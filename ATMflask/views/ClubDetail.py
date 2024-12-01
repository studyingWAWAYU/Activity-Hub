from flask import render_template, request, redirect, flash, session, url_for
from flask import Blueprint

from ATMflask import db
from ATMflask.sql import User, Participant, Activity, Membership, Club

clubdt = Blueprint('clubdt', __name__)

# 获取社团成员列表
def get_club_members(club_id):
    # 获取社团
    club = db.session.query(Club).get(club_id)

    if not club:
        return None  # 如果没有找到社团，返回None

    # 查询该社团的所有成员
    members = db.session.query(User).join(Membership).filter(Membership.club_id == club_id).all()

    return members

@clubdt.route('/ClubDetail/<int:club_id>', methods=['GET', 'POST'])
def clubDetail(club_id):
    # 获取该社团的信息
    club = db.session.query(Club).get(club_id)

    # 获取该社团的成员列表
    members = get_club_members(club_id)

    # 获取该社团的成员数量
    num_members = db.session.query(Membership).filter(Membership.club_id == club.club_id).count()

    # 获取社团的经理
    manager = db.session.query(User).join(Membership).filter(Membership.club_id == club.club_id,
                                                             Membership.role == 'manager').first()

    # 获取当前登录的用户
    user_id = session.get('id')
    is_manager = False

    if user_id:
        # 判断当前用户是否为该社团的经理
        if manager and manager.id == user_id:
            is_manager = True

    # 返回模板并传递数据
    return render_template('ClubDetail.html', club=club, manager=manager, num_members=num_members, is_manager=is_manager,members=members)

@clubdt.route('/EditClub/<int:club_id>', methods=['GET', 'POST'])
def editClub(club_id):
    # 获取该社团的信息
    club = db.session.query(Club).get(club_id)
    manager = db.session.query(User).join(Membership).filter(Membership.club_id == club.club_id,
                                                             Membership.role == 'manager').first()

    # 获取当前登录的用户
    user_id = session.get('id')
    is_manager = False

    if user_id:
        # 检查当前用户是否是社团的负责人 (manager)
        if manager and manager.id == user_id:
            is_manager = True

    if request.method == 'POST':
        # 获取用户提交的表单数据
        club_name = request.form.get('club_name')
        description = request.form.get('description')

        # 更新社团信息
        club.club_name = club_name
        club.description = description

        try:
            # 提交更新
            db.session.commit()
            flash('Club updated successfully!', 'success')
            return redirect(url_for('clubdt.clubDetail', club_id=club_id))
        except Exception as e:
            db.session.rollback()
            flash('Error updating club. Please try again.', 'danger')

    # 如果是GET请求，则渲染编辑表单
    return render_template('editClub.html', club=club,is_manager=is_manager)


@clubdt.route('/DeleteClub/<int:club_id>', methods=['GET'])
def deleteClub(club_id):
    # 获取社团信息
    club = db.session.query(Club).get(club_id)

    if not club:
        flash("Club not found.", "error")
        return redirect(url_for('clublb.clublobby'))  # 如果社团不存在，重定向到社团列表

    # 检查当前用户是否为社团经理
    user_id = session.get('id')
    if not user_id:
        flash("Please log in to delete a club.", "error")
        return redirect(url_for('auth.login'))  # 如果未登录，重定向到登录页

    # 获取该社团的经理
    manager = db.session.query(User).join(Membership).filter(Membership.club_id == club_id,
                                                             Membership.role == 'manager').first()

    if not manager or manager.id != user_id:
        flash("You are not authorized to delete this club.", "error")
        return redirect(url_for('clublb.clublobby'))  # 如果当前用户不是社团经理，重定向到社团列表

    # 删除社团及其相关信息
    try:
        # 删除社团成员关系
        db.session.query(Membership).filter(Membership.club_id == club_id).delete()
        # 删除活动关联（如果有）
        db.session.query(Activity).filter(Activity.club_id == club_id).delete()
        # 删除社团
        db.session.delete(club)
        db.session.commit()
        flash(f"Club {club.club_name} has been deleted successfully.", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred while deleting the club: {str(e)}", "error")

    return redirect(url_for('clublb.clublobby'))  # 删除后重定向到社团列表


# Release Announcement 页面
@clubdt.route('/ReleaseAnnoucement/<int:club_id>', methods=['GET', 'POST'])
def releaseAnnouncement(club_id):
    club = db.session.query(Club).get(club_id)

    if not club:
        return "Club not found", 404

    # 返回模板，传递社团信息
    if request.method == 'POST':
        # 获取公告内容
        announcement_content = request.form['announcement']

    if request.method == 'POST':
        # 获取用户提交的公告内容
        announcement_content = request.form.get('announcement')

        if announcement_content:
            # 更新社团的公告字段
            club.announcement = announcement_content
            db.session.commit()  # 提交更改到数据库

            flash('Announcement successfully released!', 'success')  # 显示成功信息
            return redirect(url_for('clubdt.clubDetail', club_id=club_id))  # 重定向到该社团的详情页面

    return render_template('ReleaseAnnoucement.html', club_name=club.club_name, club_id=club_id,club=club)




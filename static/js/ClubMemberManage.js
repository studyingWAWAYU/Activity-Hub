function confirmLogout(event) {
    event.preventDefault();  // 阻止默认行为，即阻止直接跳转
    const isConfirmed = confirm("Are you sure you want to log out?");
    if (isConfirmed) {
        window.location.href = event.target.href;  // 如果确认，执行登出操作
        document.getElementById("logoutForm").submit();
    }
}
//增加参与者
document.getElementById('add-clubmember-btn').addEventListener('click', function() {
        const userId = prompt('Enter User ID:');
        const clubId = this.dataset.clubId;
        fetch('/addClubMember', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userId,club_id:clubId})
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message);  // 显示成功消息
                location.reload();  // 刷新页面
            } else if (data.error) {
                alert(data.error);  // 显示错误消息
            }
        })
    })

// 删除参与者
const deleteButtonsNew = document.querySelectorAll('.delete-btn');
    deleteButtonsNew.forEach(button => {
        button.addEventListener('click', function() {
            // 弹出确认框
            const confirmation = confirm("Are you sure you want to delete this club member?");
            if (!confirmation) {
                return;  // 如果管理员取消删除，则返回
            }

            const userId = this.dataset.userId;
            const clubId = this.dataset.clubId;
            fetch('/deleteClubMember', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ user_id: userId, club_id:clubId})
            })
            .then(response => response.json())
            .then(data => {
                if(data.message){
                    alert(data.message);
                location.reload();
                }else if(data.error){
                    alert(data.error);
                }
            });
        });
    })

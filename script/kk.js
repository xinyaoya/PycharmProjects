$("#1equipment").on('click', function () {
    console.log("十连被点击了")
})

const equipmentBtn = $('#equipment');
equipmentBtn.on('click', function () {

    const serverID = $('#quid').val();
    const username = document.getElementById("yh").value;
    const password = document.getElementById("mm").value;
    var data = {
        "username": username,
        "pass": password,
        "ServerID": serverID
    }

    if (username !== '') {
        // 发送Ajax请求并处理响应
        $.ajax({
            type: 'post',
            url: '/api/getAndLoopAccess',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (data) {
                console.log(data);
                const img = data.message;
                layer.open({
                    type: 1,
                    title: false,
                    closeBtn: 0,
                    shadeClose: true,
                    area: ['340px', '290px'],
                    content: '<div style="padding: 20px;">' + img + '</div>',
                    end: function () {
                        // 切换页面的逻辑
                        $(".container").toggleClass("log-in");
                    }
                });
            }
        });
    } else {
        // 处理用户名为空的情况
        const serverID = $serverSelect.val();
        const json = '{"key":"value","jian":"zhi"}';
        const obj = eval("(" + json + ")");
        console.log(obj.jian);

        httpGet("http://ovooa.org/API/xiaohua/api.php", function (data) {
            layer.open({
                title: '温馨提醒',
                content: data,
                end: function () {
                    // 切换页面的逻辑
                    $(".container").toggleClass("log-in");
                }
            });
        });
    }
});
$(".info-item .btn").click(function () {
    console.log("chufale")
    $(".container").toggleClass("log-in");
});



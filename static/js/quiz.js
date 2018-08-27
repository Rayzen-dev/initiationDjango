$(function () {
    $('label.button input').on('click', function () {
        $($(this).parent()).toggleClass('active');
    });


    $(".askBar form").submit(function (e) {
        e.preventDefault();
        console.log($(this).serialize());
    });



    function question(token) {
        $.ajax({
            url: "/api/quiz",
            type: "GET",
            contentType: "application/json",
            success: function (res, stat) {
                quest = JSON.parse(res);

                //  Media
                img = document.createElement("img");
                img.setAttribute('src', quest.media);
                $('#media').html(img);

                //  Question
                $('#question').html(quest.question);

                //  Response
                str = '';
                for (var i in quest.choice) {
                    str += "<li>";
                    str += quest.choice[i].text
                    str +="</li>";
                }
                $("#response").html(str);

                //  Button
                str = "";
                count = 0;
                for (var i in quest.choice) {
                    str += "<div>" +
                        "<label class='button'>" +
                        "<input type='checkbox' value='"+quest.choice[i].value+"' name='"+String.fromCharCode(97 + count).toUpperCase()+"' />" +
                        "<span>"+String.fromCharCode(97 + count).toUpperCase()+"</span>" +
                        "</label>" +
                        "</div>";
                    count++;
                }
                $('#responseButton').html(str);
            },
            error : function(res, stat, err){
                //console.log(res)
            }
        });
    }

    question()
});

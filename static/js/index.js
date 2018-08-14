$(function () {
    $('form#chooseLicence select').on('change', function(){
        if ($(this).val().length > 0)
            getLicences($(this).val(), $(this).prev().val())
    });


    //  -----------------------------
    function getLicences(id, token) {
        $.ajax({
            url: "/api/test/"+id,
            type: "POST",
            data: {'csrfmiddlewaretoken': token},
            success: function (res, stat) {
                $('#displayLicence').empty();
                datas = JSON.parse(res);
                html = '';
                console.log(datas);

                for (var el in datas) {
                    console.log(datas[el].name)
                    html += '<div class="col-6 col-xs-12 col-sm-6"><div class="card"><p>'+datas[el].name+'</p><ul>';
                    for (var item in datas[el].data) {
                        html += '<li class="text-center">'+datas[el].data[item]+'</li>';
                    }
                    html += '</ul></div></div>';
                }
                $('#displayLicence').append(html);

            },
            error : function(res, stat, err){
                console.log(res)
            }
        })
    }
});



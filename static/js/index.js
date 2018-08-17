$(function () {
    $('form#chooseLicence select').on('change', function(){
        if ($(this).val().length > 0)
            getLicences($(this).val(), $(this).prev().val())
    });

    if ($('form#chooseLicence select').val().length > 0)
        getLicences($('form#chooseLicence select').val(), $(this).prev().val());

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

                for (var el in datas) {
                    html += '<div class="col-6 col-xs-12 col-sm-6"><div class="card"><p>'+datas[el].name+'</p><ul>';
                    html += '<li class="card__price">'+datas[el].price+' €</li>'
                    for (var item in datas[el].data) {
                        html += '<li>'+datas[el].data[item]+'</li>';
                    }
                    html += '<li><a href="/documents#documents">Documents à fournir</a></li>';
                    html += '</ul></div></div>';
                }
                $('#displayLicence').append(html);

            },
            error : function(res, stat, err){
                //console.log(res)
            }
        })
    }
});



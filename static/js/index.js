$(function () {
    $('form#chooseLicence select').on('change', function(){
        getLicences($(this).val(), $(this).prev().val())
    });


    //  -----------------------------
    function getLicences(id, token) {
        console.log(token);
        $.ajax({
            url: "/api/test/"+id,
            type: "POST",
            data: {'csrfmiddlewaretoken': token},
            success: function (res, stat) {
                console.log(res);
            },
            error : function(res, stat, err){
                console.log(res)
            }
        })
    }
});



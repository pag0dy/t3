$(document).ready(function(){
    $('.hidecard').hide();
    $('#id_account_type').unbind();
        $('#id_account_type').on('change', function(){
            if($(this).val()=='TA'){
                $('#company-fields').toggle();
            }
            else{
                $('#company-fields').fadeOut(700);
            }
        })
        $('.more').unbind();
        $('.more').on('click', function(){
            console.log($(this).val());
            $('#'+ $(this).val()).toggle("slow", function(){       
            });
        });
    $('#project_select').on('change', function(){
        $('.hideselect').hide();
        $('.' + $(this).val()).toggle();
    }).change();
});
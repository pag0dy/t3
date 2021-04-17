$(document).ready(function(){
    $('.hidecard').hide();
    $('#id_account_type').unbind();
        $('#id_account_type').on('change', function(){
            if($(this).val()=='TA'){
                $('#company-fields').fadeIn(700);
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
});
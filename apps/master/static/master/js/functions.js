$(document).ready(function(){
    $('#id_account_type').unbind();
        $('#id_account_type').on('change', function(){
            if($(this).val()=='TA'){
                $('#company-fields').fadeIn(700);
            }
            else{
                $('#company-fields').fadeOut(700);
            }
        })
});
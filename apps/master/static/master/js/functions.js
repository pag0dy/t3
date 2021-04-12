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
        $('#staff_id').on('change', function(){
            $('.card').hide();
            $('#' + $(this).val()).fadeIn(700);
        }).change();
    $('#tareas').on('click', function(){
        console.log('click!!');
        $('#form-tareas').toggle("slow", function(){       
        });
    });
});
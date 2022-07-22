let signupPhoneNum;
let secret;
let next;
let time_remaining;

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

$(document).ready(function(){
    $("#verifyPhoneNum").click(function(){
        signupPhoneNum = $("#signupPhoneNum").val();
        next = $("#next").val()

        let server_data = {
            "signupPhoneNum": signupPhoneNum
        }

        $(".spinner-border").show();

        $.ajax({
            type: "POST",
            url: $("#endpoint").val(),
            data: JSON.stringify(server_data),
            contentType: "application/json",
            dataType: 'json',
            success: function(result) {
                console.log("Result: " + result)
            }
        }).done(duringVerification())
    });

    
    function duringVerification(){
        $(".spinner-border").hide();
        $("#signupCardTitle").text("Enter verification code");
        $(".signupPhoneNum").text(signupPhoneNum);
        $("#before-verify").hide();
        $("#during-verify").show();
    
        $.getJSON({
            url: $("#signup_otp_endpoint").val(),
            data: {},
            success: function(result){
                console.log('Secret: ' + result['secret']);
                console.log('Time Remaining: ' + result['time_remaining']);
                secret = result['secret'];
                time_remaining = result['time_remaining'];
            }
        });

        $(".otpInput").keyup(function () {
            if (this.value.length == this.maxLength) {
              var $next = $(this).next('.otpInput');
              if ($next.length)
                  $(this).next('.otpInput').focus();
              else
                  $(this).blur();
            }
        });

        $("#verifyOTP").click(function(){
            console.log('OTP Submitted!');
            let OTP = $(".otpInput").map(function() {
                return $(this).val();
             }).get();
            let OTP_string = OTP.join("");
            console.log("OTP from user: " + OTP_string);    
    
            $(".spinner-border").show();
            
            $.ajax({
                type: "POST",
                url: $('#signup_otp_endpoint').val(),
                data: JSON.stringify({
                    'OTP': OTP_string,
                    'secret': secret
                }),
                contentType: "application/json",
                dataType: 'json',
                success: function(result) {
                    result_str = JSON.stringify(result);
                    console.log(typeof(result));
                    console.log("Result: " + result_str);
                    
                    if (result['response'] == true){
                        console.log("OTP from user is valid!");
                        afterVerification();
                    }
                    else {
                        $("#message").show();
                        $("#message").html('Invalid Code. Please try again.');
                        $("#message").css("color","red");
                        console.log("OTP from user is invalid!");
                    }
                }
            });
    
            $(".spinner-border").hide();
        });
    
        $("#resendOTP").click(function(){
            $(".spinner-border").show();
            duringVerification();
            $(".spinner-border").hide();
            $("#message").show();
            $("#message").html('Code has been sent.');
            $("#message").css("color","green");
        });
    };    

    function afterVerification(){
        $("#signupCardTitle").text("OTP Verified!");
        $("#during-verify").hide();
        $("#after-verify").show();

        setTimeout(function() {
            window.location.replace(next);
        }, 5000);
    }
});









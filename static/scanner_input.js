const NRIC_LENGTH = 9
let inputArr = ""

function reg_keys(){
    document.getElementById("nric_input").focus()
    window.addEventListener("keyup", event => {
        console.log("UP DETECTED")
        setTimeout(() => {
            console.log("CHECKING")
            if(document.getElementById("nric_input").value.length==NRIC_LENGTH){
                document.getElementById("nric_form").submit();
            }
        }, 500);
        
      });
    }
reg_keys()
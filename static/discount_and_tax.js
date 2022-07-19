let tax = 0.07
let discount;   

fetch('http://127.0.0.1:5000/discount').then(
        function(u){ return u.json();}
      ).then(
        function(json){
          discount = json;
          document.getElementById("discount_percent").innerHTML =("Discount (" + (discount*100).toFixed() + "%)")
        }
      )

document.getElementById("tax_percent").innerHTML =("Tax (" + (tax*100).toFixed() + "%)")
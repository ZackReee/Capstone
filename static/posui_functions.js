console.log("Barcode input script loaded.")

var sub_total = 0;
var discounted_amt = 0;
var tax_amt = 0;
var total_cost = 0;
var item_count =0;

function refocus() {
    document.getElementById("barcode_input").focus()
}

function get_cart_session() {
    fetch('http://127.0.0.1:5000/cart')
        .then(response => response.json())
        .then(data => {
            console.log("I HAVE DATA: ", data)
            makeTable(data)
          });
}

function makeTable(dt){
    mytable = document.getElementById("cart_body")
    console.log(dt)
    var row = ''
    var iter = 1
    for(var i in dt){
        console.log(i)
        row += `<tr>
                    <th scope="row">${iter}</th>
                    <td>${i}</td>
                    <td>${dt[i]["qty"]}</td>
                    <td>${dt[i]["t_price"]}</td>
                    <td><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-trash mt-1 ml-2" viewBox="0 0 16 16" onclick="remove_item(${iter-1})">
                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                    <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                  </svg></td>
                </tr>`
        iter += 1;
        console.log("What is :", dt[i]["t_price"])
        sub_total = sub_total+ parseFloat((dt[i]["t_price"]))
        item_count += dt[i]["qty"];
    }
    fill_summary();
    mytable.innerHTML = row;
    console.log("testing::::", mytable.rows[0])
}

function show_time(){
    var now = new Date();   
    // moment(now).format("Do MMMM YYYY, h:mm A")
    dateplace = document.getElementById("date_and_time")
    dateplace.innerHTML = moment(now).format("h:mm A, Do MMMM YYYY");
}

function fill_summary()
{
    discounted_amt = sub_total * discount
    tax_amt = sub_total * tax
    total_cost = sub_total - discounted_amt + tax_amt

    sub_total = round_down(sub_total)
    discounted_amt = round_down(discounted_amt)
    tax_amt = round_down(tax_amt)
    total_cost = round_down(total_cost)

    document.getElementById("subtotal_price").innerHTML = "$"+sub_total
    document.getElementById("discounted_price").innerHTML = "$"+discounted_amt
    document.getElementById("tax_price").innerHTML = "$"+tax_amt
    document.getElementById("total_price").innerHTML = "$"+total_cost
    document.getElementById("cart_count").innerHTML = item_count
    get_user_session()
}

function round_down(num){
    var n = Math.floor((num) * 100) / 100
    const rounded = parseFloat(n).toFixed(2);
    return (rounded)
}

function get_user_session() {
    fetch('http://127.0.0.1:5000/credit')
        .then(response => response.json())
        .then(data => {
            credit_remain(data)
          });
}

function credit_remain(data){
    var current = parseFloat(data)
    var remain = current - total_cost
    remain = round_down(remain)
    document.getElementById("credits_after").innerHTML = "$"+remain
    if(remain < 0){
        // document.getElementById("credits_after").innerHTML = "$0.00"
        document.getElementById("purchase_button").disabled = true
        document.getElementById("purchase_button").style.opacity= 0.5;
        document.getElementById("insufficient_credit_text").innerHTML = "Insufficient Credits. Please pay by cash."
    }
}

function remove_item(name){
    // get the name of the item then pass it to a form as value, then pass to python function.
    // py will get the item and delete from the cart sess and make a new push to /cart

    var n = document.getElementById("cart_body").rows[name].cells[1].innerHTML
    var clean_str = escape(n)
    document.getElementById("t_val").value=clean_str
    document.getElementById("remove_item_form").submit()
}

function logoutnow(){
    document.getElementById("logout_form").submit()
}

function escape(htmlStr) {
    return htmlStr.replace("&amp;", "&")}

refocus()
get_cart_session()
show_time()
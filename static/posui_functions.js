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
                </tr>`
        iter += 1;
        console.log("What is :", dt[i]["t_price"])
        sub_total = sub_total+ parseFloat((dt[i]["t_price"]))
        item_count += dt[i]["qty"];
    }
    fill_summary();
    mytable.innerHTML = row;
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

    document.getElementById("subtotal_price").innerHTML = sub_total
    document.getElementById("discounted_price").innerHTML = discounted_amt
    document.getElementById("tax_price").innerHTML = tax_amt
    document.getElementById("total_price").innerHTML = total_cost
    document.getElementById("cart_count").innerHTML = item_count
}

function round_down(num){
    var n = Math.floor((num +Number.EPSILON) * 100) / 100
    const rounded = parseFloat(n).toFixed(2);
    return (rounded)
}

function credit_remain(){
    sessino
}

function logoutnow(){
    document.getElementById("logout_form").submit()
}

refocus()
get_cart_session()
show_time()
function censor_nric(ic){
    return ic[0]+"****"+ic.slice(5, 9)
}

console.log("NRIC Censor script loaded")

function testp(){
    console.log("PRINT SUCCESS")
}
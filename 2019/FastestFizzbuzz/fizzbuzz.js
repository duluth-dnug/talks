for(var i=1; i<=1000000000; i++){
    let fizz = (i%3 == 0);
    let buzz = (i%5 == 0);
    if(fizz && buzz){
        console.log("Fizzbuzz!");
    }
    else if(fizz){
        console.log("Fizz");
    }
    else if(buzz){
        console.log("Buzz");
    }
    else{
        let s = i.toString()
        let pad = "0".repeat(10-s.length)
        console.log(pad+s)
    }
}

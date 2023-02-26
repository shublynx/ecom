

console.log("Working");

    if(localStorage.getItem("cart")==null){
        var cart = {};
         }
    else{
        cart = JSON.parse(localStorage.getItem("cart"));
        }
    $(document).on("click",".atc",function(){
        console.log("Button clicked");
        var item_id = this.id.toString()

        if(cart[item_id] != undefined){
            cart[item_id] = cart[item_id] + 1;
        }
        else{
            cart[item_id] = 1;
            }
        console.log(cart);
        localStorage.setItem("cart",JSON.stringify(cart));
    });
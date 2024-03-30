document.addEventListener("DOMContentLoaded", function() {
    var updateBtns = document.getElementsByClassName('update-cart');
    var cont = 0;

    for (var i = 0; i < updateBtns.length; i++) {
        updateBtns[i].addEventListener('click', function() {
            var productId = this.getAttribute('data-product');
            var action = this.getAttribute('data-action');
            console.log('productId:', productId, 'Action:', action);

            if (user === 'AnonymousUser') {
                cont++;
                console.log('User is not authenticated');
                if (cont > 1) {
                    document.getElementById('advertisementNotRegistredmany').style.display = 'block';
                } else {            
                    document.getElementById('advertisementNotRegistred').style.display = 'block';
                }
               
                setTimeout(function(){
                    document.getElementById('advertisementNotRegistred').style.display = 'none';
                    document.getElementById('advertisementNotRegistredmany').style.display = 'none';
                }, 3000);
            }else {
                updateUserOrder(productId, action);
            }
        });
    }
});



function updateUserOrder(productId, action){
    console.log('Sending data...')

    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}
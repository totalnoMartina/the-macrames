console.log('Hello world')

var Adding = document.getElementsByClassName('add-to-cart')

for (var i = 0; i < Adding.length; i++) {
    Adding[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
    })
}
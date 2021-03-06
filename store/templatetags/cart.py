from django import template
register = template.Library()



@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        #print(id,product.id)
        #print(type(id),type(product.id))
        if int(id) == product.id:
            return True


    #print(product,cart)

    return False


@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        #print(id,product.id)
        #print(type(id),type(product.id))
        if int(id) == product.id:
            return cart.get(id)


    #print(product,cart)

    return 0
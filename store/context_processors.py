from store.models import Cart, Category, Review


def global_context(request):
    """Add cart count and categories to all templates"""
    cart_count = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_count = cart.get_total_items()
        except Cart.DoesNotExist:
            pass
    else:
        session_key = request.session.session_key
        if session_key:
            try:
                cart = Cart.objects.get(session_key=session_key)
                cart_count = cart.get_total_items()
            except Cart.DoesNotExist:
                pass
    
    categories = Category.objects.all()
    
    # Pending reviews count for owner
    pending_reviews = 0
    if request.user.is_authenticated and (request.user.is_staff or request.user.username == 'TheDiora'):
        pending_reviews = Review.objects.filter(approved=False).count()
    
    return {
        'cart_count': cart_count,
        'categories': categories,
        'pending_reviews': pending_reviews,
    }

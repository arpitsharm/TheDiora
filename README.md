# The Diora - Premium Home Decor E-commerce Website

A modern, full-featured e-commerce platform for home decor and furniture built with Django.

## 🎨 Design Theme

**Warm Brown & Beige Color Scheme** (60-30-10 Rule)
- **60% Primary Background**: Light beige (#A69080)
- **30% Secondary**: Soft brown (#93785B)
- **10% Accent**: Dark brown (#3E362E)

## ✨ Features

### Customer Features
- ✅ User Registration & Authentication
- ✅ Product Catalog with Filtering & Search
- ✅ Shopping Cart with Coupon Support
- ✅ Wishlist Functionality
- ✅ Product Reviews & Ratings
- ✅ Secure Checkout (Cash on Delivery + Online Payment placeholder)
- ✅ Order Tracking & History
- ✅ User Profile Management

### Owner Dashboard Features
- ✅ Separate Owner Login (`/owner/login/`)
- ✅ **Analytics Dashboard**: Revenue tracking, sales statistics, top products
- ✅ **Product Management**: Add, edit, delete products with images
- ✅ **Order Management**: View orders, update status (pending → processing → delivered)
- ✅ **Customer Management**: View customer database and purchase history
- ✅ **Coupon System**: Create discount codes with percentage/fixed discounts
- ✅ **Review Moderation**: Approve/disapprove customer reviews
- ✅ **Inventory Tracking**: Low stock alerts

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

The project is already set up! Here's what was created:

1. **Django Project Structure**
   ```
   TheDiora/
   ├── manage.py
   ├── thediora/          # Django settings
   ├── store/             # Customer-facing store app
   ├── owner/             # Owner dashboard app
   ├── static/            # CSS, JS, images
   └── media/             # User uploaded files
   ```

2. **Database**: SQLite (ready to use)
3. **Dependencies**: All installed (Django 4.2, Pillow, django-crispy-forms)

### Credentials

**Owner Login:**
- URL: `http://127.0.0.1:8000/owner/login/`
- Username: `TheDiora`
- Password: `TheDiora@home`

## 📱 Website Pages

### Customer-Facing
- **Home Page** (`/`) - Hero section, featured products, categories
- **Shop** (`/products/`) - Product catalog with filters
- **Product Detail** (`/product/<slug>/`) - Full product info, reviews
- **Cart** (`/cart/`) - Shopping cart with coupon codes
- **Checkout** (`/checkout/`) - Order placement
- **Wishlist** (`/wishlist/`) - Saved products
- **Login/Register** - User authentication
- **Profile** (`/profile/`) - User settings, order history

### Owner Dashboard
- **Dashboard** (`/owner/dashboard/`) - Analytics overview
- **Products** (`/owner/products/`) - Product management
- **Orders** (`/owner/orders/`) - Order management
- **Customers** (`/owner/customers/`) - Customer database
- **Analytics** (`/owner/analytics/`) - Sales reports
- **Coupons** (`/owner/coupons/`) - Discount code management
- **Reviews** (`/owner/reviews/`) - Review moderation

## 🛍️ Payment Methods

Currently configured:
1. **Cash on Delivery (COD)** - Fully functional
2. **Online Payment** - Placeholder for future Paytm integration

**Note**: All prices are displayed in Indian Rupees (₹)

## 📊 Database Models

- **Category** - Product categories
- **Product** - Products with images, pricing, stock
- **Cart/CartItem** - Shopping cart system
- **Order/OrderItem** - Order management
- **Wishlist** - Customer wishlists
- **Review** - Product reviews & ratings
- **Coupon** - Discount codes
- **CustomerProfile** - Extended user profiles

## 🎯 Key Features Explained

### Cart System
- Session-based for guests
- User-based for authenticated customers
- Real-time total calculation
- Coupon code application

### Order Management
- Automatic order number generation (e.g., DIORA-20260330-0001)
- Status workflow: Pending → Processing → Shipped → Delivered
- Stock auto-deduction on order placement

### Coupon System
- Percentage or fixed amount discounts
- Minimum purchase requirements
- Usage limits
- Valid date ranges

### Product Management
- Image upload support
- Multiple categories
- Featured products flag
- Stock tracking
- Low stock alerts (≤5 items)

## 🎨 Styling

Modern, minimal design with:
- Responsive layout (mobile, tablet, desktop)
- Smooth animations and transitions
- Card-based UI components
- Clean typography
- Consistent color scheme throughout

## 🔧 Development Commands

```bash
# Run development server
python manage.py runserver

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic
```

## 📁 File Structure Highlights

### Store App (Customer Side)
```
store/
├── models.py          # Database models
├── views.py           # View functions
├── urls.py            # URL routing
├── forms.py           # Form classes
├── context_processors.py  # Global template variables
└── templates/store/
    ├── base.html
    ├── home.html
    ├── product_list.html
    ├── product_detail.html
    ├── cart.html
    ├── checkout.html
    ├── wishlist.html
    ├── login.html
    ├── register.html
    └── profile.html
```

### Owner App (Dashboard)
```
owner/
├── views.py           # Dashboard views
├── urls.py            # Dashboard URLs
└── templates/owner/
    ├── base.html
    ├── login.html
    ├── dashboard.html
    ├── product_list.html
    ├── product_form.html
    ├── order_list.html
    ├── order_detail.html
    ├── customer_list.html
    ├── analytics.html
    ├── coupon_list.html
    ├── coupon_form.html
    └── review_list.html
```

##  Future Enhancements

- Paytm/payment gateway integration
- Email notifications for orders
- Advanced search with Elasticsearch
- Product recommendations
- Multi-vendor support
- Blog section
- Loyalty rewards program

## 📝 Notes

- The website uses Bootstrap 5 for responsive design
- Font Awesome icons are used throughout
- Images are stored in `/media/` directory
- Static files are in `/static/` directory
- Logo is located at `logo.jpg`

## 🎉 Ready to Use!

The website is now running at: **http://127.0.0.1:8000/**

Click the preview button to view your beautiful e-commerce website!

---

**Built with ❤️ using Django**
**The Diora - Premium Home Decor**

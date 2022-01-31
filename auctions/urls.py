from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listings", views.new_listings, name="new_listings"),
    path("bid/<int:pk>", views.bid, name="bid"),
    path("categories", views.categories, name="categories"),
    path("ActiveAuctions", views.ActiveAuctions, name="ActiveAuctions"),
    path("DeActiveAuctions", views.DeActiveAuctions, name="DeActiveAuctions"),    
    path("per_category/<int:pk>", views.per_category, name="per_category"),
    path("Edit_auction/<int:pk>", views.Edit_auction, name="Edit_auction"),
    path("AuctionPerUser", views.AuctionPerUser, name="AuctionPerUser"),
    path("Add_watchlist/<int:pk>", views.Add_watchlist, name="Add_watchlist"),    
]
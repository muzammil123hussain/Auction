import auctions
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


from .models import Bids, Category, Comments, User, listings, watchlist


def index(request):
        auction_list = listings.objects.filter(active=1)
        return render(request, "auctions/index.html",{
            'auction_list' : auction_list
            })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def new_listings(request):
    if request.method == "POST":
        try:
            title = request.POST["title"]
            Description = request.POST["Description"]
            price = request.POST["price"]
            cat = request.POST["cat"]
            active = request.POST.get("active")
            if active is None:
                active = 0

            category = Category.objects.get(id=cat)

            new_list = listings.objects.create(user=request.user,title=title,description=Description, starting_price=price, category=category, active=active)
            new_list.save()
            return HttpResponseRedirect(reverse("index"))

        except IntegrityError:
            category = Category.objects.all().order_by('category')
            return render(request, "auctions/new_listings.html", {
                "message": "Item already taken.",
                'category' : category
            })
        except Exception as e:
            category = Category.objects.all().order_by('category')
            return render(request, "auctions/new_listings.html", {
                "message": str(e),
                'category' : category
            })
    else:
        category = Category.objects.all().order_by('category')
        return render(request, "auctions/new_listings.html",{
            'category' : category
        })

def bid(request, pk):

    if request.method == "POST":
        try:
            bid_price = request.POST["bid"]
            comment = request.POST["comment"]
            time = datetime.now()
        
            Bids.objects.create(user=request.user, bid_price=bid_price, auction_id=pk, bid_time=time)
            Comments.objects.create(user=request.user, comments=comment, auction_id=pk)

            return redirect(index)
        except Exception as e:
            auction_list = listings.objects.get(id=pk)
            category = Category.objects.get(id=auction_list.category_id)
            bids_list = Bids.objects.filter(auction_id=pk)
            return render(request, "auctions/bid.html", {
                "message": str(e),
                'id' : pk,
                'auction_list' : auction_list,
                'category' : category,
                'bids_list' : bids_list
            })
    else:
        auction_list = listings.objects.get(id=pk)
        category = Category.objects.get(id=auction_list.category_id)
        bids_list = Bids.objects.filter(auction_id=pk)
        return render(request, "auctions/bid.html", {
            'id' : pk,
            'auction_list' : auction_list,
            'category' : category,
            'bids_list' : bids_list
            })

def categories(request):
        cat_list = Category.objects.all()
        return render(request, "auctions/categories.html",{
            'cat_list' : cat_list           
            })

def per_category(request, pk):
        auction_list = listings.objects.filter(category_id=pk)
        return render(request, "auctions/per_category.html", 
            {'id' : pk, 'auction_list' : auction_list}
        )

def ActiveAuctions(request):
        Active_list = listings.objects.filter(user_id=request.user.id, active=1)
        return render(request, "auctions/ActiveAuctions.html", {'Active_list' : Active_list})

def DeActiveAuctions(request):
        De_Active_list = listings.objects.filter(user_id=request.user.id, active=0)
        return render(request, "auctions/DeActiveAuctions.html", {'De_Active_list' : De_Active_list})

def Edit_auction(request, pk):
    if request.method == "POST":
        try:
            title = request.POST["title"]
            Description = request.POST["Description"]
            price = request.POST["price"]
            cat = request.POST["cat"]
            active = request.POST.get("active")
            if active is None:
                active = 0

            category = Category.objects.get(id=cat)

            update_list = listings.objects.filter(id=pk).update(user=request.user,title=title,description=Description, starting_price=price, category=category, active=active)
            return HttpResponseRedirect(reverse("AuctionPerUser"))

        except Exception as e:
            category = Category.objects.all().order_by('category')
            return render(request, "auctions/new_listings.html", {
                "message": str(e),
                'category' : category
            })
    else:
        category = Category.objects.all().order_by('category')
        auction_item = listings.objects.get(id=pk)
        return render(request, "auctions/Edit_auction.html",{
            'category' : category,
            'pk' : pk,
            'auction_item' : auction_item
        })

def AuctionPerUser(request):
    all_acution_list = listings.objects.filter(user_id=request.user.id)
    return render(request, "auctions/AuctionPerUser.html",{
        'all_acution_list' : all_acution_list
    })

def Add_watchlist(request,pk):
    if request.method == "POST":
        active = 1
        add = watchlist.objects.create(user_id=request.user.id,auction_id=pk,active=active)
        print(add)
        return redirect(index)
    else:
        print("not add")
        return redirect(index)





    
read -p "Please give the app_id?" appid
read -p "Please give the app_secret" appsec
read -p "Please give the short lived User Token for the app" token
wget "https://graph.facebook.com/v2.2/oauth/access_token?grant_type=fb_exchange_token&client_id=$appid&client_secret=$appsecret&fb_exchange_token=$token"
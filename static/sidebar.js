var para = document.getElementsByClassName("sidebar")[0];

para.innerHTML = ' \
<style> @import "/static/sidebar.css"; </style> \
<!-- MOSTLY SKIDDED FROM https://www.w3schools.com/howto/howto_js_sidenav.asp --> \
<div id="mySidenav" class="sidenav"> \
    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a> \
    <a href="/">Home</a> \
    <a href="/lobbies.html#">Lobbies</a> \
    <a href="/gravity.html#">Gravity</a> \
    <a href="/survivalgames.html#">Survival Games</a> \
    <a href="/deathrun.html#">Death Run</a> \
    <a href="/hideandseek.html#">Hide and seek</a> \
    <a href="/skywars.html#"> Skywars </a> \
    <a class="small" href="/skywars.html#solo">Skywars solo</a> \
    <a class="small" href="/skywars.html#duo">Skywars duo</a> \
    <a class="small" href="/skywars.html#4s">Skywars 4s</a> \
    <a href="/TIMV.html#">Trouble in Mineville</a> \
    <a href="/splegg.html#">Splegg</a> \
    <a href="/bedwars.html#">Bedwars</a> \
    <a class="small" href="/bedwars.html#nixarko">Nix/Arko (owners)</a> \
    <a class="small" href="/bedwars.html#matze">Matze (other)</a> \
    <a href="/arcade.html#">Arcade</a> \
    <a class="small" href="/arcade.html#cranked">Cranked</a> \
    <a class="small" href="/arcade.html#electricfloor">Electric Floor</a> \
    <a class="small" href="/arcade.html#instagib">Instagib</a> \
    <a class="small" href="/arcade.html#oitc">OITC</a> \
    <a class="small" href="/arcade.html#slaparoo">Slaparoo</a> \
    <a class="small" href="/arcade.html#sloop">Sloop</a> \
    <a class="small" href="/arcade.html#splegg">Splegg</a> \
    <a class="small" href="/arcade.html#batterydash">Battery Dash</a> \
  </div> \
  <div class="open" onclick="openNav()">≡</div><br><br> \
'

/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
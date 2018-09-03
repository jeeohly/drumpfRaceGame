# Lee Gio (gl9qd) CS 1111, fall 2016
# tan5um, CS1111, Fall 2016
import pygame
import gamebox
import random
import string
import re

camera = gamebox.Camera(800, 600)
character = gamebox.from_image(50, 200, "http://lh3.googleusercontent.com/gIK4nwfl8oIf2-HMxxueyleceXQ486IoMM1NxCkFIyWMxRzB42J2-QqQdmYe2GvOYUoC=w80")
character.scale_by(0.6)

character.yspeed = 0
electorates = [['Alabama', 9], ['Alaska', 3], ['Arizona', 11], ['Arkansas', 6], ['California', 55], ['Colorado', 9], ['Connecticut', 7], ['Delaware', 3], ['Florida', 29], ['Georgia', 16], ['Hawaii', 4], ['Idaho', 4], ['Illinois', 20], ['Indiana', 11], ['Iowa', 6], ['Kansas', 6], ['Kentucky', 8], ['Louisiana', 8], ['Maine', 4], ['Maryland', 10], ['Massachusetts', 11], ['Michigan', 16], ['Minnesota', 10], ['Mississippi', 6], ['Missouri', 10], ['Montana', 3], ['Nebraska', 5], ['Nevada', 6], ['New-Hampshire', 4], ['New-Jersey', 14], ['New-Mexico', 5], ['New-York', 29], ['North-Carolina', 15], ['North-Dakota', 3], ['Ohio', 18], ['Oklahoma', 7], ['Oregon', 7], ['Pennsylvania', 20], ['Rhode-Island', 4], ['South-Carolina', 9], ['South-Dakota', 3], ['Tennessee', 11], ['Texas', 38], ['Utah', 6], ['Vermont', 3], ['Virginia', 13], ['Washington', 12], ['West-Virginia', 5], ['Wisconsin', 10], ['Wyoming', 3]]

walls = [
    gamebox.from_image(50, 250, "http://i.imgur.com/BzEpZzN.png"),
    gamebox.from_image(400, 150, "http://i.imgur.com/BzEpZzN.png"),
    gamebox.from_image(600, 25, "http://i.imgur.com/BzEpZzN.png"),
]

counter = 0
coins = []
damages = []
time = 0
score = 0
health = 100
bernie_health = 100
states_gained = []
state_names = []
results = []
stars = []
trump_lasers = []
clinton_lazers = []
bernie_lazers = []
bosses = []
health_packs = []
nras = []
mexicans = []
width = 50
bernie_width = 50
reload_width = 50
seconds = 0
hillary_kills = 0
boss_time = 250
reload_time = 10
nra_time = 60
z=0
shots = 50
reloads = 0
trump_walls = 0
startscreen = True

#music
defeat = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/c/cf/Baby_long_wanting_cry.ogg")
defeat2 = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/6/67/Arcane_Battle.ogg")
victory = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/6/65/Star_Spangled_Banner_instrumental.ogg")
coin_sound = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/c/c5/Aboiement.ogg")
dmg_sound = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/3/36/9_237_50_10_50_10_138_1_1_32_1_8_0_100_100_1SequenBaul.ogg")
lazer_sound = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/5/51/20_237_50_10_50_10_138_1_1_32_1_20_0_100_100_1SequenBaul.ogg")

def tick(keys):
    # get access to the counter

    global health
    global bernie_health
    global time, score
    global number
    global results
    global width
    global bernie_width
    global reload_width
    global seconds
    global hillary_kills
    global boss_time, reload_time
    global z
    global shots
    global reloads
    global trump_walls
    global startscreen

    if (startscreen == True):                                       #Startscreen stuff
        camera.clear("blue")
        gameTitle = gamebox.from_text(400, 130, "Trump's Race to 270", "Arial Black", 50, "red")
        names = gamebox.from_text(400, 180, "Gio Lee and Alex Nguyen", "Arial Black", 25, "white")
        IDs = gamebox.from_text(400, 215, "gl9qd and tan5um", "Arial Black", 20, "blue")
        Instructions1 = gamebox.from_text(400, 280, "CONTROLS", "Arial Black", 40, "red")
        Instructions2 = gamebox.from_text(400, 320, "Left and Right keys to move", "Arial Black", 25, "white")
        Instructions3 = gamebox.from_text(400, 350, "Up key to shoot", "Arial Black", 25, "white")
        Instructions4 = gamebox.from_text(400, 380, "SPACE to jump", "Arial Black", 25, "white")
        Instructions5 = gamebox.from_text(400, 420, "Collect 270 Electoral Votes", "Arial Black", 25, "blue")
        Instructions6 = gamebox.from_text(400, 460, "Avoid Dumbocrats", "Arial Black", 25, "red")
        Instructions7 = gamebox.from_text(400, 500, "Pess SPACE to play", "Arial Black", 25, "white")
        startBack = gamebox.from_image(400, 300, "https://static1.squarespace.com/static/56d888de2eeb810551cf2ede/t/572388741bbee05672165552/1461946494425/American-Flag-Dark.png")

        camera.draw(startBack)
        camera.draw(Instructions1)
        camera.draw(Instructions2)
        camera.draw(Instructions3)
        camera.draw(Instructions4)
        camera.draw(Instructions5)
        camera.draw(Instructions6)
        camera.draw(Instructions7)
        camera.draw(gameTitle)
        camera.draw(names)
        camera.draw(IDs)
        camera.display()
        if (pygame.K_SPACE in keys):
            startscreen = False

    else:
        if health > 0 and camera.y + 300 > character.y and score < 270:
            time +=1
        seconds = str(int((time / ticks_per_second))).zfill(3)
        int_seconds = int(seconds)
        global counter
        if health > 0 and camera.y + 300 > character.y and score < 270:
            if pygame.K_RIGHT in keys:
                character.x += 10
            if pygame.K_LEFT in keys:
                character.x -= 10
        character.yspeed += 1
        character.y = character.y + character.yspeed
        camera.clear("black")
        camera.y -= 3
        counter += 1

        #space_background = gamebox.from_image(camera.x, camera.y, "http://i.imgur.com/IaZSnb6.jpg")
        #camera.draw(space_background)

        #stars
        if counter % 3 == 0:
            numstars = random.randint(0, 7)
            for i in range(numstars):
                stars.append(gamebox.from_image(camera.x + random.randint(-395, 395), camera.y - random.randint(5, 695), "http://i.imgur.com/mkRBUQc.png"))

        for star in stars:
            if star.y > camera.y + 300:
                stars.remove(star)
            star.y += 3
            if (star.y > 600):
                stars.remove(star)
            camera.draw(star)

        camera.draw(character)

        #chances
        if counter % 50 == 0:
            chances_of_moving_wall = random.randint(1, 3)
            chances_of_health_pack = random.randint(4, 8)
            wall_position = random.randint(200, 600)
            if chances_of_moving_wall == 2:
                moving_wall = gamebox.from_image(wall_position, camera.y - 300, "http://i.imgur.com/W8lihGR.png")
                moving_wall.speedx = 5
                walls.append(moving_wall)
            else:
                new_wall = gamebox.from_image(wall_position, camera.y - 300, "http://i.imgur.com/BzEpZzN.png")
                walls.append(new_wall)
            if chances_of_health_pack == 5:
                health_pack = gamebox.from_image(wall_position, camera.y -335, "http://i.imgur.com/K9XCw5f.png")
                if chances_of_moving_wall == 2:
                    health_pack.speedx = 5
                health_packs.append(health_pack)
            if chances_of_health_pack == 4:
                nra = gamebox.from_image(wall_position, camera.y - 345, "http://i.imgur.com/s3zwqsR.png")
                nra.scale_by(0.75)
                if chances_of_moving_wall == 2:
                    nra.speedx = 5
                nras.append(nra)
            if chances_of_health_pack == 7:
                mexican = gamebox.from_image(wall_position, camera.y - 350, "http://i.imgur.com/rS727NA.png")
                if chances_of_moving_wall == 2:
                    mexican.speedx = 5
                mexicans.append(mexican)
        #walls
        for wall in walls:
            if wall.y > camera.y + 325:
                walls.remove(wall)
            if wall.speedx != 0:
                if wall.speedx > 0 and wall.x > 650:
                    wall.speedx = -5
                if wall.speedx < 0 and wall.x < 150:
                    wall.speedx = 5
                wall.move_speed()
            if character.bottom_touches(wall):
                character.yspeed = 0
                if health > 0 and camera.y + 300 > character.y and score < 270:
                    if pygame.K_SPACE in keys:
                        character.yspeed = -20
                if wall.speedx != 0:
                    character.speedx = wall.speedx
                    character.move_speed()
            if character.touches(wall):
                character.move_to_stop_overlapping(wall)
            camera.draw(wall)

        # healthbar
        background = gamebox.from_color(character.x, character.y - 35, "red", 50, 5)
        health_bar2 = gamebox.from_color(character.x - ((50 - width) / 2), character.y - 35, "green", width, 5)
        # boss
        if time > boss_time and time < boss_time+60 and time%20 == 0:
            preboss = gamebox.from_image(400, camera.y - 200, "http://i.imgur.com/k8zOYcp.png")
            preboss.yspeed = -3
            preboss.scale_by(0.5)
            preboss.move_speed()
            camera.draw(preboss)
        if time == boss_time+60:
            boss = gamebox.from_image(400, camera.y - 200, "http://i.imgur.com/Gv62x02.png")
            boss.scale_by(0.5)
            boss.yspeed = -3
            boss.speedx = 5
            bosses.append(boss)
        for boss in bosses:
            if boss.speedx > 0 and boss.x > 750:
                boss.speedx = -5
            if boss.speedx < 0 and boss.x < 50:
                boss.speedx = 5
            boss.move_speed()
            if health > 0:
                camera.draw(boss)
            if character.touches(boss):
                dmg_sound.play()
            if character.touches(boss):
                dmg_sound.play()
                health = 0
                character.image = "http://i.imgur.com/BQ3iFnZ.png"
                bosses.remove(boss)
                width = 0
            if time % 60 == 0:
                bernie_lazer = gamebox.from_image(boss.x, boss.y + 75, "http://i.imgur.com/7mhtj3f.png")
                bernie_lazer.yspeed = 5
                clinton_lazers.append(bernie_lazer)
            #boss healthbar
            boss_background = gamebox.from_color(boss.x, boss.y - 50, "red", 50, 5)
            boss_healthbar = gamebox.from_color(boss.x - ((50 - bernie_width) / 2), boss.y - 50, "green", bernie_width, 5)
            camera.draw(boss_background)
            camera.draw(boss_healthbar)
        # damage
        if time % 60 == 0:
            dmg_x = random.randint(200, 600)
            dmg_y = camera.y - 300
            dmg = gamebox.from_image(dmg_x, dmg_y - 50, "http://i.imgur.com/aSxhgf2.png")
            dmg.speedx = 3
            damages.append(dmg)
        for dmg in damages:
            if dmg.y > camera.y + 300:
                damages.remove(dmg)
            if dmg.speedx != 0:
                if dmg.speedx > 0 and dmg.x > 775:
                    dmg.speedx = -3
                if dmg.speedx < 0 and dmg.x < 25:
                    dmg.speedx = 3
            dmg.move_speed()
            if character.touches(dmg):
                dmg_sound.play()
                if health != 0:
                    health -= 10
                    width -= 5
                if health <= 50 and health != 0:
                    character.image = "http://i.imgur.com/wGfiqcN.png"
                if health == 0:
                    character.image = "http://i.imgur.com/BQ3iFnZ.png"
                damages.remove(dmg)
            if health > 0 and camera.y + 300 > character.y and score < 270:
                camera.draw(dmg)
            if time % 60 == 0:
                clinton_lazer = gamebox.from_image(dmg.x, dmg.y + 25, "http://i.imgur.com/QtabVAK.png")
                clinton_lazer.yspeed = 5
                clinton_lazers.append(clinton_lazer)
        for clinton in clinton_lazers:
            if clinton.y > camera.y + 300:
                clinton_lazers.remove(clinton)
            clinton.move_speed()
            camera.draw(clinton)
            if character.touches(clinton):
                dmg_sound.play()
                if health != 0:
                    health -= 10
                    width -= 5
                if health <= 50 and health != 0:
                    character.image = "http://i.imgur.com/wGfiqcN.png"
                if health == 0:
                    character.image = "http://i.imgur.com/BQ3iFnZ.png"
                clinton_lazers.remove(clinton)

        #coins
        if time % 60 == 0:
            coin_x = random.randint(200, 600)
            coin_y = camera.y - 300
            votes = random.randint(0, len(electorates) - 1)
            states_gained.append(electorates[votes][1])
            state = str(electorates[votes][0]).lower()
            state_names.append(state)
            state_picture = gamebox.from_image(coin_x, coin_y, "http://global.fncstatic.com/static/p/elections/2016/img/elections/states/"+state+".png")
            state_picture.scale_by(0.2)
            coins.append(state_picture)

        for coin in coins:
            if coin.y > camera.y + 300:
                coins.remove(coin)
            if time % 60 == 0:
                regex = re.compile(r"([\,\.][-.\d]?[0-9][0-9][0-9]?[0-9]?)")
                result = regex.findall(str(coin))
                result = result[0]
                result = int(result[1:])
                if result not in results:
                    results.append(result)
            if character.touches(coin):
                regex = re.compile(r"([\,\.][-.\d]?[0-9][0-9][0-9]?[0-9]?)")
                result2 = regex.findall(str(coin))
                result2 = result2[0]
                result2 = int(result2[1:])
                for x in range (0, len(results)):
                    if results[x] == result2:
                        y = x
                        score += states_gained[y]
                        print(state_names[y], states_gained[y])
                coin_sound.play()
                coins.remove(coin)
            if health > 0 and camera.y + 300 > character.y and score < 270:
                camera.draw(coin)

        #health packs
        for health_pack in health_packs:
            if health_pack.y > camera.y + 300:
                health_packs.remove(health_pack)
            if health_pack.speedx != 0:
                if health_pack.speedx > 0 and health_pack.x > 650:
                    health_pack.speedx = -5
                if health_pack.speedx < 0 and health_pack.x < 150:
                    health_pack.speedx = 5
                health_pack.move_speed()
            camera.draw(health_pack)
            if character.touches(health_pack) and health != 0:
                health_packs.remove(health_pack)
                if health < 100:
                    health += 10
                    width += 5
            if health >= 50:
                character.image = "http://lh3.googleusercontent.com/gIK4nwfl8oIf2-HMxxueyleceXQ486IoMM1NxCkFIyWMxRzB42J2-QqQdmYe2GvOYUoC=w80"

        #NRAs
        for nra in nras:
            if nra.y > camera.y + 300:
                nras.remove(nra)
            if nra.speedx != 0:
                if nra.speedx > 0 and nra.x > 650:
                    nra.speedx = -5
                if nra.speedx < 0 and nra.x < 150:
                    nra.speedx = 5
                nra.move_speed()
            camera.draw(nra)
            if character.touches(nra):
                reloads += 1
                nras.remove(nra)
        if reloads > 0:
            shots = 10
            fedora = gamebox.from_image(character.x, character.y -18, "http://i.imgur.com/0rzGP8D.png")
            fedora.scale_by(0.9)
            camera.draw(fedora)
            high_noon = gamebox.from_text(150, camera.y - 265, "ITS HIGH NOON (" + str(reloads) + ")", "Arial Black", 15, "white")
            camera.draw(high_noon)
        if reload_width == 0 and shots == 10:
            if time == z + reload_time:
                reloads -= 1
        if reloads == 0:
            shots = 50

        #mexicans
        for mexican in mexicans:
            if mexican.y > camera.y + 300:
                mexicans.remove(mexican)
            if mexican.speedx != 0:
                if mexican.speedx > 0 and mexican.x > 650:
                    mexican.speedx = -5
                if mexican.speedx < 0 and mexican.x < 150:
                    mexican.speedx = 5
                mexican.move_speed()
            camera.draw(mexican)
            if character.touches(mexican):
                trump_walls += 3
                mexicans.remove(mexican)
        trump_wall = gamebox.from_image(character.x, character.y, "http://i.imgur.com/YJm72Jb.png")
        trump_wall.scale_by(0.7)
        if trump_walls > 0:
            trump_wall_text = gamebox.from_text(650, camera.y - 265, "TRUMP WALLS (" + str(trump_walls) + ")", "Arial Black", 15, "white")
            camera.draw(trump_wall_text)
            camera.draw(trump_wall)
            for clinton in clinton_lazers:
                if clinton.touches(trump_wall):
                    trump_walls -= 1
                    clinton_lazers.remove(clinton)
            for dmg in damages:
                if dmg.touches(trump_wall):
                    damages.remove(dmg)
                    trump_walls -= 3
        if trump_walls < 0:
            trump_walls = 0

        #texts
        time_box = gamebox.from_text(725, camera.y - 285, "Time: " + seconds, "Arial Black", 15, "white")
        score_box = gamebox.from_text(75, camera.y - 285, "Votes: " + str(score), "Arial Black", 15, "red")
        hillary_kills_box = gamebox.from_text(400, camera.y - 285, "Dumbocrat Kills: " + str(hillary_kills), "Arial Black", 15, "blue")
        topbar = gamebox.from_color(400, camera.y - 285, "dark gray", 800, 15)
        #health_bar = gamebox.from_text(character.x, character.y - 35, "Health: " + str(health) + "%", "Arial Black", 10, "white")
        #low_health = gamebox.from_text(400, camera.y - 275, "Health: " + str(health) + "%", "Arial Black", 24, "light coral")
        #no_health = gamebox.from_text(400, camera.y - 275, "Health: " + str(health) + "%", "Arial Black", 24, "red")
        gameover = gamebox.from_text(400, camera.y, "CROOKED HILLARY WINS", "Arial Black",40, "blue")
        gameover2 = gamebox.from_text(400, camera.y, "THE ELECTION WAS RIGGED", "Arial Black", 40, "blue")
        win = gamebox.from_text(400, camera.y, "MAKE AMERICA GREAT AGAIN", "Arial Black", 40, "red")
        final_time = gamebox.from_text(400, camera.y + 50, "Your final time was "+str(int_seconds)+" seconds", "Arial Black", 15, "white")
        final_kills = gamebox.from_text(400, camera.y + 75, "You killed " + str(hillary_kills) + " dumbocrats", "Arial Black", 15, "white")
        #if health > 50:
            #camera.draw(health_bar)
        #if health <= 50:
            #camera.draw(low_health)
        #if health == 0:
            #camera.draw(no_health)

        # trump lazer
        reload = gamebox.from_color(character.x - ((50-reload_width)/2), character.y - 27, "yellow", reload_width, 3)
        if pygame.K_UP in keys:
            trump_laser = gamebox.from_image(character.x, character.y - 35, "http://i.imgur.com/OheiEOS.png")
            trump_laser.scale_by(0.5)
            if reload_width != 0:
                trump_lasers.append(trump_laser)
                reload_width = reload_width - shots
        for laser in trump_lasers:
            laser.yspeed = -30
            laser.move_speed()
            camera.draw(laser)
            if reload_width == 0:
                z = time
            if laser.y < camera.y - 300:
                trump_lasers.remove(laser)
            for dmg in damages:
                if laser.touches(dmg):
                    lazer_sound.play()
                    damages.remove(dmg)
                    for laser in trump_lasers:
                        trump_lasers.remove(laser)
                    hillary_kills += 1
            for boss in bosses:
                if laser.touches(boss):
                    lazer_sound.play()
                    for laser in trump_lasers:
                        trump_lasers.remove(laser)
                    bernie_health -= 10
                    bernie_width -= 5
                if bernie_health == 0:
                    bosses.remove(boss)
                    hillary_kills += 10
                    boss_time = time + 250
                    bernie_health = 100
                    bernie_width = 50
        if time == z + reload_time:
            reload_width = 50
        camera.draw(reload)

        #gameover
        if score >= 270:
            camera.draw(win)
            camera.draw(final_time)
            camera.draw(final_kills)
            victory.play()
        elif health <= 0:
            camera.draw(gameover)
            camera.draw(final_time)
            camera.draw(final_kills)
            defeat.play()
        elif camera.y + 300 < character.y:
            camera.draw(gameover2)
            camera.draw(final_time)
            camera.draw(final_kills)
            defeat2.play()
            #gamebox.stop_loop()

        camera.draw(background)
        camera.draw(health_bar2)
        camera.draw(topbar)
        camera.draw(time_box)
        camera.draw(score_box)
        camera.draw(hillary_kills_box)
        camera.display()

ticks_per_second = 30
pygame.display.set_caption("Trump's Race to 270")
gamebox.timer_loop(ticks_per_second, tick)

from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("MAZE")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

hero = Hero(size_window[0] // 2 - size_hero[0] // 2,size_window[1] - size_hero[1] - 20,size_hero[0],size_hero[1],hero_image_list,5, 5)

background = Background(size_background[1], background_image, 2)

game = True
start_time_bot = 0
end_time_bot = 0

while game:
    if hero.hp < 0:
        game = False
    events = pygame.event.get()
    
    background.move(window)
    hero.move(window)

    render_text_hp = font.render(f"x{hero.hp}", True, RED) 
    render_kill_bot = font.render(f"x{hero.kill_bot}", True, RED) 
    window.blit(heart_image_list, (10,10))
    window.blit(skull_image_list, (500,10))
    window.blit(render_text_hp, (65,25))
    window.blit(render_kill_bot, (555,25))

    for bot in bot_list:
        bot.move(window)
        bot.shoot_bot(end_time_bot)

    end_time_bot = pygame.time.get_ticks()
    if end_time_bot - start_time_bot > 2000:
        start_time_bot = end_time_bot
        bot_list.append(Bot(randint(0, size_window[0] - size_bot[0]), - size_bot[1], size_bot[0], size_bot[1], bot_image_list, 2))

    for bullet in bullet_list_hero:
        bullet.move(window)
    for bullet in bullet_list_bot:
        bullet.move(window)

#ffffffffffffffff
    for bot in bot_list:
        if bot.colide_hero(bullet_list_hero):
            hero.kill_bot += 1

#ffffffffffffffffffffffff
#if index_buff != -1:
#    Buff.buff_list[index_buff].completing()
    for buf in Buff.buff_list:
        buf.move(window)
        buf.collide(hero, bot_list)
        if buf.active:
            buf.work_time(end_time_bot, hero)
#fffffffffffffffff

    hero.colide_enemy(bot_list)
    hero.colide_enemy(bullet_list_bot)
    index_buff = hero.colide_buff(Buff.buff_list)

    for event in events:
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                hero.walk["left"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                hero.walk["left"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                hero.walk["right"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                hero.walk["right"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and hero.can_shoot:
                bullet_list_hero.append(Bullet(hero.centerx - 5, hero.y, 10, 20, RED, hero.speed_bulet, None))
                hero.can_shoot = False



    clock.tick(FPS)
    pygame.display.flip()
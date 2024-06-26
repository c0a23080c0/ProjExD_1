import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    se_bg_img = pg.transform.flip(bg_img,True,False)
    kouk_img = pg.image.load("fig/3.png")
    kouk_img = pg.transform.flip(kouk_img,True,False)    
    tmr = 0
    kouk_rct = kouk_img.get_rect()
    kouk_rct.center =  300 , 200
    tate = 0
    yoko = -1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(se_bg_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(se_bg_img, [-x+4800, 0])

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            tate = -1
        if key_lst[pg.K_DOWN]:
            tate = 1
        if key_lst[pg.K_RIGHT]:
            yoko = 1
        if key_lst[pg.K_LEFT]:
            yoko = -2
        kouk_rct.move_ip(yoko,tate)
        tate = 0
        yoko = -1
        screen.blit(kouk_img,kouk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
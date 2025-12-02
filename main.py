@namespace
class SpriteKind:
    HUD = SpriteKind.create()
# Final interactivo
def elegirDestinoFinal():
    pass
def mostrarInstrucciones():
    game.show_long_text("¡Bienvenido a la fábrica de estrellas!", DialogLayout.FULL)
    game.show_long_text("Presiona (A) repetidamente para recolectar partículas y evolucionar tu estrella.",
        DialogLayout.FULL)
    game.show_long_text("Cada fase necesita cierta cantidad de partículas para avanzar.",
        DialogLayout.FULL)
    game.show_long_text("Pulsa (B) para abrir la tienda y comprar mejoras para recolectar más rápido.",
        DialogLayout.FULL)
    game.show_long_text("Al llegar a gigante roja, ¡podrás elegir su destino final!",
        DialogLayout.FULL)
# Cambiar de fase con efectos
def cambiarFase(nombre: str, imagen: Image, escala: number, explosionSize: number):
    global p
    estrella.set_image(imagen)
    estrella.set_scale(escala, ScaleAnchor.MIDDLE)
    mostrarFase(nombre)
    # effects.confetti.startScreenEffect(500)
    music.power_up.play()
    # game.showLongText("¡Has formado una " + nombre + "!", DialogLayout.Bottom)
    for index in range(explosionSize):
        p = sprites.create(image.create(4, 4), SpriteKind.projectile)
        p.image.fill(9)
        p.set_position(estrella.x, estrella.y)
        p.set_velocity(randint(-50, 50), randint(-50, 50))
        p.lifespan = 400
# Recolectar partículas con A

def on_a_pressed():
    global particulas, particle
    particulas += 1 * multiplicador
    actualizarEstatus()
    particle = sprites.create(image.create(4, 4), SpriteKind.projectile)
    particle.image.fill(2)
    particle.set_position(randint(0, 160), randint(0, 120))
    particle.set_velocity((estrella.x - particle.x) / 10,
        (estrella.y - particle.y) / 10)
    particle.lifespan = 500
    music.play_tone(523, music.beat(BeatFraction.SIXTEENTH))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# Abrir tienda con B

def on_b_pressed():
    tiendaMejoras()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def iniciarJuego():
    global particulas, fase, multiplicador, textoLinea1, textoLinea2, estrella, musicaEncendida, hudLinea1, hudLinea2
    particulas = 0
    fase = 0
    multiplicador = 1
    textoLinea1 = ""
    textoLinea2 = ""
    estrella = sprites.create(img("""
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            ffffffffffffffffffffffffffffccccccfffffffffffff.
            ffffffffffffffffffffffffffffccccccfffffffffffff.
            ffffffffffffffffffffffffffffccccccfffffffffffff.
            ffffffffffffffffffffffccccccfffffffffffffffffff.
            ffffffffffffffffffffffccccccfffffffffffffffffff.
            ffffffffffffffffffffffccccccfffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffccccccfffccccccfffffffffffffffffff.
            fffffffffffffccccccfffccccccfffffffffffffffffff.
            fffffffffffffccccccfffccccccfffffffffffffffffff.
            fffffffffffffffffffcccbbbcccfffffffffffffffffff.
            fffffffffffffffffffbbbbbbcccffffffcccffffffffff.
            fffffffffffffffffffbbbbbbcccffffffcccffffffffff.
            fffffffffcccfffccccbbbdddbbbbbbbbbccccfffffffff.
            fffffffffcccfffccccbbbdddbbbbbbbbbccccccfffffff.
            fffffffffcccfffccccbbbdddbbbbbbbbbccccccfffffff.
            fffffffffcccfffccccbbbdddbbbbbbbbbccccccfffffff.
            ffffffcccffffcccfffddd111dddcccffffffffffffffff.
            ffffffcccffffcccfffddd111dddcccffffffffffffffff.
            ffffffcccfffccccfffbbbddddddcccffffffffffffffff.
            ffffffffffffcbbcfffcccbbbccccccffffffffffffffff.
            ffffffffffffcbbcfffcccbbbccccccffffffffffffffff.
            ffffffffffffcbbcfffcccbbbccccccffffffffffffffff.
            fffffffffffffffffffcccbbbcccbbbffffffffffffffff.
            fffffffffffffffffffcccbbbcccbbbffffffffffffffff.
            fffffffffffffffffffcccbbbcccbbbffffffffffffffff.
            fffffffffffffffffffcccfffffffffffffffffffffffff.
            fffffffffffffffffffcccfffffffffffffffffffffffff.
            fffffffffffffffffffcccfffffffffffffffffffffffff.
            fffffffffcccffffffffffcccffffffffffffffffffffff.
            fffffffffcccffffffffffcccffffffffffffffffffffff.
            fffffffffcccffffffffffcccffffffffffffffffffffff.
            ffffffffffffffffffffffcccffffffffffffffffffffff.
            ffffffffffffffffffffffcccffffffffffffffffffffff.
            ffffffffffffffffffffffcccffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            fffffffffffffffffffffffffffffffffffffffffffffff.
            """),
        SpriteKind.player)
    musicaEncendida = 0
    estrella.set_position(80, 60)
    estrella.set_scale(1.5, ScaleAnchor.MIDDLE)
    hudLinea1 = sprites.create(image.create(80, 8), SpriteKind.HUD)
    hudLinea2 = sprites.create(image.create(80, 8), SpriteKind.HUD)
    hudLinea1.set_position(80, 2)
    hudLinea2.set_position(80, 24)
    hudLinea1.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    hudLinea2.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    game.splash("¡Bienvenido a la fábrica de estrellas! Presiona A para recolectar partículas.")
    if not (musicaEncendida == 1):
        music.set_volume(50)
        music.play(music.string_playable("C5 B A G F E D C ", 120),
            music.PlaybackMode.UNTIL_DONE)
        musicaEncendida = 1
# Mostrar nombre de fase en dos líneas, sin encimarse
def mostrarFase(nombre2: str):
    global linea1, linea2, textoLinea1, textoLinea2
    if nombre2 == "estrella principal":
        linea1 = "estrella"
        linea2 = "principal"
    elif nombre2 == "estrella joven":
        linea1 = "estrella"
        linea2 = "joven"
    elif nombre2 == "gigante roja":
        linea1 = "gigante"
        linea2 = "roja"
    else:
        linea1 = nombre2
        linea2 = ""
    if linea1 != textoLinea1:
        hudLinea1.say(linea1)
        textoLinea1 = linea1
    if linea2 != textoLinea2:
        hudLinea2.say(linea2)
        textoLinea2 = linea2
# Actualizar estado del juego
def actualizarEstatus():
    global fase
    info.set_score(particulas)
    if particulas >= 0 and particulas < 20 and fase < 1:
        fase = 1
        cambiarFase("nebulosa",
            img("""
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                ffffffffffffffffffffffffffffccccccfffffffffffff.
                ffffffffffffffffffffffffffffccccccfffffffffffff.
                ffffffffffffffffffffffffffffccccccfffffffffffff.
                ffffffffffffffffffffffccccccfffffffffffffffffff.
                ffffffffffffffffffffffccccccfffffffffffffffffff.
                ffffffffffffffffffffffccccccfffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffccccccfffccccccfffffffffffffffffff.
                fffffffffffffccccccfffccccccfffffffffffffffffff.
                fffffffffffffccccccfffccccccfffffffffffffffffff.
                fffffffffffffffffffcccbbbcccfffffffffffffffffff.
                fffffffffffffffffffbbbbbbcccffffffcccffffffffff.
                fffffffffffffffffffbbbbbbcccffffffcccffffffffff.
                fffffffffcccfffccccbbbdddbbbbbbbbbccccfffffffff.
                fffffffffcccfffccccbbbdddbbbbbbbbbccccccfffffff.
                fffffffffcccfffccccbbbdddbbbbbbbbbccccccfffffff.
                fffffffffcccfffccccbbbdddbbbbbbbbbccccccfffffff.
                ffffffcccffffcccfffddd111dddcccffffffffffffffff.
                ffffffcccffffcccfffddd111dddcccffffffffffffffff.
                ffffffcccfffccccfffbbbddddddcccffffffffffffffff.
                ffffffffffffcbbcfffcccbbbccccccffffffffffffffff.
                ffffffffffffcbbcfffcccbbbccccccffffffffffffffff.
                ffffffffffffcbbcfffcccbbbccccccffffffffffffffff.
                fffffffffffffffffffcccbbbcccbbbffffffffffffffff.
                fffffffffffffffffffcccbbbcccbbbffffffffffffffff.
                fffffffffffffffffffcccbbbcccbbbffffffffffffffff.
                fffffffffffffffffffcccfffffffffffffffffffffffff.
                fffffffffffffffffffcccfffffffffffffffffffffffff.
                fffffffffffffffffffcccfffffffffffffffffffffffff.
                fffffffffcccffffffffffcccffffffffffffffffffffff.
                fffffffffcccffffffffffcccffffffffffffffffffffff.
                fffffffffcccffffffffffcccffffffffffffffffffffff.
                ffffffffffffffffffffffcccffffffffffffffffffffff.
                ffffffffffffffffffffffcccffffffffffffffffffffff.
                ffffffffffffffffffffffcccffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                fffffffffffffffffffffffffffffffffffffffffffffff.
                """),
            1.5,
            1)
    elif particulas >= 20 and particulas < 50 and fase < 2:
        fase = 2
        cambiarFase("protoestrella",
            img("""
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffeeeeeeeeeeeeeeefffffffff
                ffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeefffffff
                fffffffffffffffffeeeeeeee22eeeeeeeeeeeeeeeeeffffff
                fffffffffffffffeeeeee2e22222222222e222eeeeeeefffff
                fffffffffffffeeeeeee224444444444442e222eeeeeefffff
                ffffffffffffeeeeeee22445dd5444444442222eeeeeefffff
                ffffffffffeeeeeee244445d1ddd544444442e2eeefeffffff
                fffffffffeeeeee2444445dd111d554444444eeeeeeeffffff
                ffffffffeeeeeee4444445d11111d54444442eeeefeeffffff
                fffffffeeeeeee2444444dd11111d5444442eeeefeeeffffff
                ffffffeeeeeee24444444dd1111d5544442eeeeeeeefffffff
                ffffffeeeeee2444455444dd1dd5444442eeeeeeefffffffff
                fffffee2eeee244445555445d54444422eeeeeeeffffffffff
                fffffee2eeeee224444444444442222eeeeeeeefffffffffff
                fffffeeeeeeeeeeee22222222224eeeeeeeeffffffffffffff
                ffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffff
                fffffffeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffff
                ffffffffeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffff
                fffffffffffeeeeeeeeeeeeeffffffffffffffffffffffffff
                fffffffffffffeeeeeeeffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                """),
            1.7,
            2)
    elif particulas >= 50 and particulas < 100 and fase < 3:
        fase = 3
        cambiarFase("estrella joven",
            img("""
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                fffffffffffeeeffffffffffeefffffffffffeffffffffffff
                fffffffffffeeeeffffffffceeffffffffffeeffffffffffff
                ffffffffffffeeeffffffffe44eefffffffcefffffffffffff
                ffffffffffffeeeffffeeee4444eeeffffeeefffffffffffff
                fffffffffffffffeeee44445554444eeeeeeffffffffffffff
                fffffffffffffffeee455555555544444effffffffffffffff
                fffffffffffffffeee455555555545444effffffffffffffff
                fffffffffffffffe44455555555554444effffffffffffffff
                ffffffffffffffe4445555555555554444eecfffffffffffff
                ffffffffffffffe4555555dd555555555444efffffffffffff
                ffffffffffffffe4555555dd555555555444efffffffffffff
                ffffffffffffffe555555dddd55555555444efffffffffffff
                ffffffceeeee444555555dddd555555554444eeeeeeeffffff
                ffffeee44444555555555ddddd55555555444444444eeeefff
                fffffeeeeeee4445555555ddd555555554444eeeeeeeeeefff
                ffffffffffffee455555555dd555555554444cffffffffffff
                ffffffffffffeee455555555555555555444efffffffffffff
                ffffffffffffffe45555555555555555444ecfffffffffffff
                ffffffffffffffe4445555555555554444eeffffffffffffff
                ffffffffffffffe4445555555555544444eeffffffffffffff
                ffffffffffffffce444555555555544444eeffffffffffffff
                fffffffffffffffe44444555555544444effffffffffffffff
                fffffffffffffffeeee44444444444eeeeeeffffffffffffff
                ffffffffffffffeefffee44444444ecffeeecfffffffffffff
                ffffffffffffffeefffee44444444efffe4eefffffffffffff
                ffffffffffffeeefffffffee44eecfffffceefffffffffffff
                fffffffffffeeeffffffffffeefffffffffffeffffffffffff
                fffffffffffeeeffffffffffeefffffffffffeffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                ffffffffffffffffffffffffeeffffffffffffffffffffffff
                """),
            2,
            3)
    elif particulas >= 100 and particulas < 200 and fase < 4:
        fase = 4
        cambiarFase("estrella principal",
            img("""
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffcffffffffffffffffffffffffff
                fffffffffffffffeeffffff4efff4ffffffffffffffffffff
                ffffffffffffffff44fffff42ffff4ffffeffffffffffffff
                fffffffffffffffff24eff4444ff44ffff24fffffffffffff
                fffffffffffffffff444fe2544f444fffe24fffffffffffff
                ffffffffff444ffff444444544444fffe244fffffffffffff
                fffffffff4e444fff455445555454ef2444ffffffffffffff
                fffffffffff44444455555555555544444ffff2ffffffffff
                ffffffffffff4544455444444444455554ee444ffffffffff
                ffffffffffff45555544445555444455544454fffffffffff
                fffffffffcfff555445555555555544455554cffffeffffff
                ffffff44ffff4554455555555555555445552fffffeffffff
                fffffe4444e44544555555555555555544552ffff2effffff
                fffff4ff4544554555555555555555555455444444fffffff
                fffffffff45554455555115555555555544554444ffffffff
                fffffffff4454455555111555555555554455554effffffff
                ffffffefff45455555511155555555555544544ffffffffff
                fffffffff445455555555555555555555544544ffffffffff
                ffffffe42455455555555555555555555554544ff4effffff
                fffff4444455455555555555555555555554554444effffff
                ffff4ff24555455555555555555555555454555444fffffff
                ffffffffe45545555555555555555555555455544ffffffff
                ffffffffff45455555555555555555555544544ffffffffff
                ffffffefff45545555555555555555555545544ff4fffffff
                ffffffff4455545555555555555555545445554ffffffffff
                fffffff445555445455555555555555554455554ff4ffffff
                ffffff444444554555555555555555554455444424cffffff
                ffffff44ff445544554555555555455544554ce44ffffffff
                ffffffeffff4455445554455555455444554fffffffffffff
                ffffffcfeff4455544555454445555445554fefffffffffff
                ffffffffff445455554445555554445554454ffffffffffff
                ffffffffff444445555444444444455554444ef4fffffffff
                fffffffff442ffc4544555555555544454ff444ffffffffff
                fffffffff4ffffe4444455555555544c44ff44effffffffff
                ffffffffffffff444ff45444454454ff444ffffffffffffff
                ffffffffffffff44cff4544f454444fff44efffffffffffff
                ffffffffffffffe4fff44ffff44f44fffffffffffffffffff
                ffffffffffffffc4fff44ffff4ffe44cfffffffffffffffff
                fffffffffffffffffffff4fffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                """),
            2.5,
            4)
    elif particulas >= 200 and fase < 5:
        fase = 5
        cambiarFase("gigante roja",
            img("""
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffff2222fffffffffffffffffffffff
                fffffffffffffffffffff2222222fffffffffffffffffffff
                fffffffffffffff22ff2222222222ffefffffffffffffffff
                ffffffffffffffff2222222422222222fffffffffffffffff
                ffffffffffffffee222224444444422222fffffffffffffff
                ffffffffffffe22222244442222244422222ff2ffffffffff
                fffffffffff2222224422222222222242222f22ffffffffff
                ffffffffffff22244444444442222222442222fffffffffff
                ffffffffffff2444224444444442222224422ffffffffffff
                ffffffffff2224224444445544222222222222fffffffffff
                fffffffff222422444555445542444422222222ffffffffff
                ffffffff2222424445555544542244422222222ffffffffff
                ffffffff22242444555554444222424222222222fffffffff
                ffffffff22242424555544444222242222222222fffffffff
                fffffff222442424555442442244442222e2e2222ffffffff
                fffffff22242244444444422422222222ee2ee2222fffffff
                fffffff2224224244244222244222222e222ee2222fffffff
                ffffff2222422222442222224222222222eeee2222fffffff
                ffffff222242242222244444422222222eeeee2222fffffff
                ffffffe222222444422444422222222e22e2ee222ffffffff
                fffffff222422222444422222222222222eee2222ffffffff
                fffffff22242222222222222222e22e222eee2222ffffffff
                ffffffff224422222222222222eeee22eeeee222fffffffff
                ffffffff22242e22222222222ee222222efee222fffffffff
                fffffffff2242e22222222222e222222ffffe222fffffffff
                fffffffff2222ee222222222e22e222ef2fe222efffffffff
                ffffffff2e2222ee2222222e222222eeffe222fffffffffff
                fffffffeff22222eee222222222ffffff2222ffffffffffff
                fffffffffff22222eeeeeee22fffffff2222fffffffffffff
                ffffffffffff22222eeeeeeeeff22ff22222fffffffffffff
                fffffffffffff222222feeeee22eff222222fffffffffffff
                fffffffffffffe22222222eeeee2222222e22ffffffffffff
                fffffffffffffffff2222222222222effffffffffffffffff
                ffffffffffffffffff2ff22222222efffffffffffffffffff
                ffffffffffffffffffffff22222ffffffffffffffffffffff
                ffffffffffffffffffffffff22fffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff
                """),
            3,
            6)
        pause(2000)
        elegirDestinoFinal()
# Tienda de mejoras
def tiendaMejoras():
    global particulas, multiplicador
    game.splash("Tienda de mejoras", "Presiona A para comprar mejoras")
    if particulas >= 50 and multiplicador == 1:
        particulas += 0 - 50
        multiplicador = 2
        game.show_long_text("¡Mejora activada! ahora cada clic vale el doble.",
            DialogLayout.CENTER)
    elif particulas >= 100 and multiplicador == 2:
        particulas += 0 - 100
        multiplicador = 3
        game.show_long_text("¡Mejora activada! ahora cada clic vale el triple.",
            DialogLayout.CENTER)
    elif particulas >= 200 and multiplicador == 3:
        particulas += 0 - 200
        multiplicador = 5
        game.show_long_text("¡Mejora activada! ahora cada clic vale x5.",
            DialogLayout.CENTER)
    else:
        game.show_long_text("¡No tienes suficientes partículas o ya has mejorado al máximo!",
            DialogLayout.CENTER)
    info.set_score(particulas)
star: Sprite = None
linea2 = ""
linea1 = ""
hudLinea2: Sprite = None
hudLinea1: Sprite = None
musicaEncendida = 0
textoLinea2 = ""
textoLinea1 = ""
fase = 0
particle: Sprite = None
multiplicador = 0
particulas = 0
p: Sprite = None
estrella: Sprite = None
opcion = ""
mostrarInstrucciones()
iniciarJuego()

def on_update_interval():
    global star
    star = sprites.create(image.create(2, 2), SpriteKind.food)
    star.image.fill(1)
    star.set_position(randint(0, 160), 0)
    star.vy = randint(10, 30)
    star.lifespan = 4000
game.on_update_interval(300, on_update_interval)

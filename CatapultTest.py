import Catapult

cat = Catapult.SimpleCatapult()

cat.DEBUG = True

def spacing():
    print("")
    print("")

print("Arming and disarming...")
cat.arm()
cat.disarm()
spacing()

print("disarm firing...")
cat.fire()
spacing()

print("arming and firing...")
cat.arm()
cat.fire()
spacing()

print("double arming...")
cat.arm()
cat.arm()
spacing()


print("resetting tension and firing...")
cat.changeTension(99)
cat.fire()
spacing()

print("setting tension, arming, and firing...")
cat.changeTension(1)
cat.arm()
cat.fire()
spacing()

print("setting yaw, arming, and firing...")
cat.changeYaw(100)
cat.arm()
cat.fire()
spacing()

print("arming, setting yaw, and firing...")
cat.arm()
cat.changeYaw(10)
cat.fire()
spacing()

print("setting angle, arming, and firing...")
cat.changeAngle(100)
cat.arm()
cat.fire()
spacing()

print("arming, setting angle, and firing...")
cat.arm()
cat.changeAngle(10)
cat.fire()
spacing()

print("feeding changeTension garbage...")
cat.changeTension(False)
cat.changeTension(-100)
cat.changeTension(1.1)
cat.changeTension(cat)
cat.changeTension("null")
spacing()

print("feeding changeAngle garbage...")
cat.changeAngle(False)
cat.changeAngle(-100)
cat.changeAngle(1.1)
cat.changeAngle(cat)
cat.changeAngle("null")
spacing()

print("feeding changeYaw garbage...")
cat.changeYaw(False)
cat.changeYaw(-100)
cat.changeYaw(1.1)
cat.changeYaw(cat)
cat.changeYaw("null")
spacing()

print("mangling the catapult lock state in armed mode...")
cat.arm()
cat.isLocked = False
cat.fire()
spacing()

print("mangling the catapult lock state in disarmed mode...")
cat.isLocked = True
cat.arm()
cat.fire()
spacing()

print("magling the catapult lock state in armed mode...")
cat.arm()
cat.isLocked = False
cat.fire()
spacing()

print("mangling the catapult tension in armed mode...")
cat.arm()
cat.isTense = False
cat.fire()
spacing()

print("mangling the catapult tension in disarmed mode...")
cat.isTense = True
cat.arm()
cat.fire()
spacing()

print("mangling the catapult armed bool in armed mode...")
cat.arm()
cat.isArmed = False
cat.fire()
spacing()

print("mangling the catapult armed bool in disarmed mode...")
cat.isArmed = True
cat.arm()
cat.fire()
spacing()

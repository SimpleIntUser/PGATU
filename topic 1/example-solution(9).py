def artorom(arabic):
  match arabic:
      case 1:
          RTZ = "I"
      case 2:
          RTZ = "II"
      case 3:
          RTZ = "III"
      case 4:
          RTZ = "IV"
      case 5:
          RTZ = "V"
      case 6:
          RTZ = "VI"
      case 7:
          RTZ = "VII"
      case 8:
          RTZ = "VIII"
      case 9:
          RTZ = "IX"
    return RTZ
print(def(int(input("введите арабское число от 1 до 9: ")))

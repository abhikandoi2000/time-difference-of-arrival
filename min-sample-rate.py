error = (8*np.pi)/180# radians
distance=10 # meters
seperation = 0.05*np.sqrt(2) # meters
print(seperation)

sourcePos1 = np.array([[distance],[0],[1]])
sourcePos2 = np.array([[distance*np.cos(error)],[distance*np.sin(error)],[1]])
mic1 = np.array([[-seperation/2],[0],[0]])
mic2 = np.array([[seperation/2],[0],[0]])

ddoa_true = np.linalg.norm(sourcePos1-mic1) - np.linalg.norm(sourcePos1-mic2)
ddoa_got = np.linalg.norm(sourcePos2-mic1) - np.linalg.norm(sourcePos2-mic2)

print(ddoa_true, ddoa_got)

print((ddoa_true-ddoa_got)*100) # centimeters


print(1500/(ddoa_true-ddoa_got)) # required ADC sampling rate in Hz
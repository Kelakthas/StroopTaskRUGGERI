datastroop = read.csv ("C:/Users/randy/OneDrive/Favoris/Documents/Etudes/Post-bac/Psychologie - Master/M2/Progamming/ProjectStroopCode_35_202405290931.xpd", skip=10, header = TRUE)

datastroop$respkey[datastroop$respkey==98]="BLUE"
datastroop$respkey[datastroop$respkey==114]="RED"
datastroop$respkey[datastroop$respkey==121]="YELLOW"
datastroop$respkey[datastroop$respkey==103]="GREEN"

datastroop$coherence [datastroop$TARGET==datastroop$Colour.de.la.target]="Coherent"
datastroop$coherence [datastroop$TARGET!=datastroop$Colour.de.la.target]="Incoherent"

datastroop$reponse [datastroop$respkey==datastroop$Colour.de.la.target]="Vrai"
datastroop$reponse [datastroop$respkey!=datastroop$Colour.de.la.target]="Faux"

MeanCoh = mean(datastroop$RT[datastroop$coherence=="Coherent"])
MeanIncoh = mean(datastroop$RT[datastroop$coherence=="Incoherent"])
MeanCoh = round(MeanCoh, digits = 2)
MeanIncoh = round(MeanIncoh, digits = 2)

print(paste("Voilà la moyenne du temps de réaction lorsque le stimulus est cohérent :", MeanCoh))
print(paste("Voilà la moyenne du temps de réaction lorsque le stimulus n'est pas cohérent :", MeanIncoh))

Test = t.test(datastroop$RT[datastroop$coherence=="Coherent"],datastroop$RT[datastroop$coherence=="Incoherent"])
print (Test)
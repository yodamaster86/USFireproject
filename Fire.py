from pydoc import visiblename
from turtle import color
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import datetime as dt
import plotly.express as px
import matplotlib.dates as mdates


primaryColor="#F63366"
backgroundColor="#262730"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"


st.set_page_config(page_title= "Investigation Feux de forêt aux Etats-Unis", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

######### Barre de séléction latérale
st.sidebar.header("Analyse des feux de forêt aux USA ")

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.markdown('---')
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")

st.sidebar.write("Thème")
st.write("***")
themes = st.sidebar.selectbox("Quelle thématique voulez vous choisir?",["Page d'acceuil","Analyse temporelle","Analyse spatiale",
                              "Effet de la météorologie","Causes","Machine learning"])
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.write("Par:")
st.sidebar.write("Paul Dorcier, Martin Honoré Faussi et Thomas-Oshagan Haladjian")

intro = pd.read_csv(r"C:\Users\thoma\Data\DFstreamlit.csv",index_col='Unnamed: 0')
df =  pd.read_csv(r"C:\Users\thoma\Data\demo.csv")
xx=pd.read_csv(r"C:\Users\thoma\Data\x.csv")
r=pd.read_csv(r"C:\Users\thoma\Data\r.csv")
v=pd.read_csv(r"C:\Users\thoma\Data\v.csv")
df['grand_ou_petit']= ['petit' if ((taille == 'A') or (taille == 'B') or (taille== 'C')) else 'grand' for taille in df['FIRE_SIZE_CLASS']]
Grandfeu= df.loc[df['grand_ou_petit']=='grand']
Petitfeu= df.loc[df['grand_ou_petit']=='petit']

############################################ PAGE D ACCEUIL #########################
if themes == "Page d'acceuil":
    st.title("Analyse des feux de forêt aux Etats-Unis de 1992 à 2015")
    image = Image.open(r"C:\Users\thoma\Data\firemen2.jpg")
    st.image(image, caption='Feux de forêt aux USA')
    st.header("Contexte")
    st.write("")
    st.write("")
    st.write("Notre analyse se base sur un jeu de données receuillant des données de 1992 à 2015 sur les feux de forêt aux Etats-Unis.")
    st.write("Le jeu de données brut contient plus d'1.88 million de ligne pour 33 colonnes contenant diverses informations tel que le lieu de l'incendie, sa taille ou sa cause")
    st.write("Le but de notre analyse a été d'essayer de déterminer le facteurs influencant le nombre et la taille de ces incendies.")
    st.write("Le jeu de données utilisé est le suivant:")
    st.write("")
    st.dataframe(intro.head(20))


#######################################Analyse temporelle####################################
elif themes == "Analyse temporelle":
     st.markdown("<h1 style='text-align: center; color: black;'>Nombre d'incendie par jours sur la durée de l'étude</h1>", unsafe_allow_html=True)     
     st.write("")
     st.write("")
     fig, ax = plt.subplots(figsize=(20,8))
     sns.lineplot( x = 'date',  y = 'val_rol', data=xx,  label = 'moyenne mobile',color='blue',ax=ax)
     plt.title("Nombre de feux de forêt par date",fontsize=14)
     plt.xlabel("date",fontsize=12)
     plt.ylabel("nombre d'incendies",fontsize=12)
     years = mdates.YearLocator()
     ax.xaxis.set_major_locator(years)
     plt.xticks(rotation=60)
     st.pyplot(fig, figsize=(20,8),use_container_width=True)


     st.write("")
     st.write("")
     st.write("---")
     st.title("Evolution du nombre et de la taille des incendies par an et par Etat par rapport à la moyenne nationale")
     st.write("")
     st.write("")
 
     sns.set()
     fig_2, (ax1, ax2,ax3,ax4) = plt.subplots(4, figsize=(30,50))
     ##### Nombre d'incendie par ans pour les etats qui en ont le plus
     
     
     dff = df.loc[(df['STATE']=="CA")|(df['STATE']=="GA")|(df['STATE']=="TX")|(df['STATE']=="NC")|(df['STATE']=="FL")|(df['STATE']=="SC"),:]

     sns.lineplot(x='FIRE_YEAR', y='FOD_ID', hue='STATE',data=dff.groupby(['STATE', 'FIRE_YEAR']).count(), ax=ax1)
     sns.lineplot(x='FIRE_YEAR', y='count', data=r, linestyle='dashed',color='red', label='moyenne nationale', ax=ax1);
     ax1.set_ylabel('nombre d incendie')
     ax1.set_xlabel('annee')
     ax1.set(title='Nombre d incendie par an pour les 6 Etats qui ont le plus d incendies')

     ######### Taille moyenne des incendies pour les états qui en ont le plus

     sns.lineplot(x='FIRE_YEAR', y='FIRE_SIZE', hue='STATE',data=dff.groupby(['STATE','FIRE_YEAR']).mean(),ax=ax3)
     sns.lineplot(x='FIRE_YEAR', y='mean', data=v, linestyle='dashed',color='red', label='moyenne nationale',ax=ax3);
     ax3.set_ylabel('taille moyenne des incendies incendie')
     ax3.set_xlabel('annee')
     ax3.set_title('Taille moyenne des incendies pour les 6 Etats qui ont le plus d incendies')

     dfff = df.loc[(df['STATE']=="IL")|(df['STATE']=="IN")|(df['STATE']=="RI")|(df['STATE']=="VT")|(df['STATE']=="DE")|(df['STATE']=="DC"),:]

     sns.lineplot(x='FIRE_YEAR', y='FOD_ID', hue='STATE',data=dfff.groupby(['STATE', 'FIRE_YEAR']).count(),ax=ax2)
     sns.lineplot(x='FIRE_YEAR', y='count', data=r, linestyle='dashed',color='red', label='moyenne nationale',ax=ax2);
     ax2.set_ylabel('nombre d incendie')
     ax2.set_xlabel('annee')
     ax2.set_title('Nombre d incendie par an pour les 6 Etats qui ont le moins d incendies')
     plt.legend();
 
     sns.lineplot(x='FIRE_YEAR', y='FIRE_SIZE', hue='STATE',data=dfff.groupby(['STATE','FIRE_YEAR']).mean(),ax=ax4)
     sns.lineplot(x='FIRE_YEAR', y='mean',data=v, linestyle='dashed',color='red', label='moyenne nationale',ax=ax4);
     ax4.set_ylabel('taille moyenne des incendies incendie')
     ax4.set_xlabel('annee')
     ax4.set_title('Taille moyenne des incendies pour les 6 Etats qui ont le moins d incendies');
     st.pyplot(fig_2, figsize=(25,40), use_container_width=False)
     st.write("")
     st.markdown("---")
     st.write("")

     col1, col2 = st.columns(2)
     
     with col1:
         st.header("Nombre d'incendie total par mois")
         fig_3,ax5= plt.subplots(figsize=(15,8))
         col = df["MOIS"].value_counts().sort_index()
         col = col.rename({"1":'janvier',"2":'février','3':'mars','4':'avril','5':'mai','6':'juin','7':'juillet','8':'août',
                  '9':'septembre','10':'octobre','11':'novembre','12':'décembre'}, axis=0)
         plt.title("Nombre total d incendie pour chaque mois entre 1992 et 2015")
         for tick in ax1.get_xticklabels():
               tick.set_rotation(60)        
         sns.barplot(x=col.index,y=col, order = col.index, ax=ax5)
         plt.ylabel("nombre d'incendie")
         plt.xlabel('mois')

         st.pyplot(fig_3, use_container_width=False)
         
         with col2:
           st.header("Taille moyenne des incendies par mois")
           fig_4,ax6= plt.subplots(figsize=(15,8))
           
           tri = df.groupby('MOIS')['FIRE_SIZE'].mean()
           tri = tri.rename({"1":'janvier',"2":'février','3':'mars','4':'avril','5':'mai','6':'juin','7':'juillet','8':'août',
                  '9':'septembre','10':'octobre','11':'novembre','12':'décembre'})
           
           sns.barplot(tri.index,tri.values,ax=ax6);
           plt.title('Taille moyenne des incendies en fonction du mois');
           plt.xticks(rotation=20);
           plt.ylabel('taille moyenne de l incendie (acre)')
           plt.xlabel('mois')
           st.pyplot(fig_4, use_container_width=False)
           
     st.write("")
     st.markdown("---")    
     st.write("")
     st.header("Combien y a t-il eu de feux de forêt de grande taille (>300 acres) par mois?")
     st.write("")      
     c=df.groupby(['MOIS','FIRE_SIZE_CLASS'])['FIRE_SIZE_CLASS'].count().reset_index(name="count")
     c=pd.DataFrame(c)
     c.MOIS = c.MOIS.replace({"01":'janvier',"02":'février','03':'mars','04':'avril','05':'mai','06':'juin','07':'juillet','08':'août','09':'septembre','10':'octobre','11':'novembre','12':'décembre'})

     c = c.loc[(c['FIRE_SIZE_CLASS']=='E')|(c['FIRE_SIZE_CLASS']=='F')|(c['FIRE_SIZE_CLASS']=='G')]

     fig4 = px.bar(c, x="FIRE_SIZE_CLASS", y="count", animation_frame='MOIS', title = "Nombre d'incendies par catégorie de taille de feu", labels={"FIRE_SIZE_CLASS":"classe de taille","count":"nombre d'incendies"}, width=800, height=600)
     
     st.plotly_chart(fig4, use_container_width=True)
    
     
     ###########################################################################################""
elif themes == "Analyse spatiale":
     st.title("Analyse des paramètres géographiques sur les feux de forêt aux USA")
     st.write(" ")
     st.markdown("---")
     st.write(" ")
     st.subheader("Nombre total de feux de forêt sur la période 1992-2015 en fonction des états")
     max_col = df['STATE'].value_counts().head(8).to_frame(name = "count")
     min_col = df["STATE"].value_counts().tail(8).to_frame(name = "count")

     fig5 = px.bar(x=max_col.index, y=max_col["count"], title ="Nombre de feux de forêt pour les 8 Etats  en ayant eu le plus", labels={'x':'Etats',"y":'Nombre d incendies'})     
     st.plotly_chart(fig5, use_container_width=True)
     st.write("CA = California, GA = Georgia, TX = Texas, NC = North Carolina, FL = Florida, SC = South Carolina, NY = New York, MS = Mississipi ")
     st.markdown("---")
     st.write(" ")
     fig6 = px.bar(x=min_col.index, y=min_col["count"], title ="Nombre de feux de forêt pour les 8 Etats  en ayant eu le moins", labels={'x':'Etats',"y":'Nombre d incendies'})     
     st.plotly_chart(fig6, use_container_width=True)
     st.write("MA = Massaschusset, NH = New Hampshire, IL= Illinois, ID = Indiana, RI = Rhodes Island, VT = Vermont, DE = Deleware, DC = Washington DC")
     st.write(" ")
     st.markdown("---")
     st.write(" ")
     
     st.write("**Carte réprésentation des feux de plus de 100 acres (0.4km2)**")

     dfmap3=Grandfeu.sort_values('FIRE_SIZE_CLASS')
     fig_map3 = px.scatter_mapbox(dfmap3,
                                   lat="LATITUDE",
                                   lon="LONGITUDE",
                                   animation_frame="FIRE_YEAR",
                                   color='FIRE_SIZE_CLASS',
                                   zoom=2,
                                   mapbox_style="open-street-map",
                                   width=1000,
                                   height=600)  

     st.plotly_chart(fig_map3, use_container_width=True)
     fig_map4.update_layout(legend_title_text='Taille des feux')

#################################################################################################################""
elif themes == "Effet de la météorologie":
    st.title("Effet de la météorologie")
    st.write(" ")
    st.write(" ")
    st.write("Intuitivement on pourrait penser qu'il y a un lien entre la météorologie et le nombre ou la taille des feux de forêt.")
    st.write("C'est ce que nous avons voulu vérifier en réccupérant les données météo (température moyenne et pluviométrie moyenne)"
             "de l'année 1993 en Californie et nous l'avons comparé à nos données.")

    dT= df.loc[(df['FIRE_YEAR']==1993) & (df['STATE']=='CA')]
    dT = dT.sort_values(by='MOIS',ascending=True)
    
    nb=dT.groupby(['MOIS'])['FOD_ID'].count().to_frame(name = 'count')

    fig_7=px.line(nb, x=nb.index, y=nb['count'], title = "nombre d incendie par mois en 1993 en Californie", labels={'x':'mois','y':'nombre d incendies'})
    st.plotly_chart(fig_7, use_container_width=True)


    Temp=np.array([6.86,13.83,20.17,24.56,26.79,32.55,31.82,32.6,31.68,25.2,16.72,14.04])
    yy=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    fig_9 = px.line(x=yy, y=Temp, markers=True, title="Température moyenne par mois", labels={'x':'mois','y':'température moyenne'})
    st.plotly_chart(fig_9, use_container_width=True)
    
    precip=np.array([26.7208,14.63,4.64,0,0,1.87,0,0,0,0.279,2.36,2.69])
    yy=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    fig_8 = px.line(x=yy, y=precip, markers=True, title="Précipitation (cm) par mois", labels={'x':'mois','y':'précipitation (cm)'})
    st.plotly_chart(fig_8, use_container_width=True)
    
    st.write("")
    st.markdown("---")

    st.header('Droite de corrélation')
    nb['Temp']=Temp
    nb['precip']=precip
    fig9,ax11 = plt.subplots(figsize=(10, 6))
    sns.regplot(x='Temp',y='count',data=nb,order=1,ci=None,ax=ax11)
    plt.title('Relation entre le nombre d incendie et la température')
    plt.xlabel('température')
    plt.ylabel('nombre d incendies')
    st.plotly_chart(fig9, use_container_width=True)
    st.write("                                                     Le coefficient de Pearson vaut **0.86**")
    st.write(" ")
    
    fig10,ax12 = plt.subplots(figsize=(10, 6))
    sns.regplot(x='precip',y='count',data=nb,order=1,ci=None,ax=ax12)
    plt.title('Relation entre le nombre d incendie et la pluviométrie')
    plt.xlabel('précipitations')
    plt.ylabel('nombre d incendies')
    st.plotly_chart(fig10, use_container_width=True)
    st.write("                                                      Le coefficient de Pearson vaut **-0.56**")

     
   ###################################################################################################################""
elif themes == "Causes":  
    st.title("Quelles ont été les causes les plus fréquences de feux de forêt aux USA de 1992 à 2015?")
    def filtre (i):
       if i =="Powerline" :
         return 'Powerline/Firework'
       elif i=='Fireworks':
         return 'Powerline/Firework'
       elif i=="Structure":
         return 'Powerline/Firework'
       else :
         return i
    df.STAT_CAUSE_DESCR = df.STAT_CAUSE_DESCR.apply(filtre)
    agg_cause = df.groupby(['STAT_CAUSE_DESCR'])['FOD_ID'].count()

    agg_cause = agg_cause.sort_values(ascending=False)

    fig11 = px.pie(agg_cause, values=agg_cause.values, names=agg_cause.index, title="Causes en fonction de leur pourcentage d occurence", width=800, height=600)
    st.plotly_chart(fig11, use_container_width=True)
    st.write(" ")
    st.markdown("---")
    st.write(" ")
    st.subheader("Cherchons désormais à voir la cause des incendies en fonction de leur taille")
    
    
    GrandfeuCause = Grandfeu.groupby(['FIRE_SIZE_CLASS', 'STAT_CAUSE_DESCR']).agg({'FOD_ID': 'count'})
    Grandfeu_pcts = GrandfeuCause.groupby(level=0).apply(lambda x:
                                                 100 * x / x.sum()).rename({'FOD_ID': 'count'}, axis=1).reset_index()
                                              
    fig12 = px.bar(Grandfeu_pcts, x="FIRE_SIZE_CLASS", y="count", color="STAT_CAUSE_DESCR", title="Causes des incendies pour les grands feux",labels={"FIRE_SIZE_CLASS":"Classe de taille", "count":"Nombre d'incendies"},height=500, width=600)
    fig12.update_layout(legend_title_text='Cause des feux')
    st.plotly_chart(fig12, use_container_width=True)

    PetitfeuCause = Petitfeu.groupby(['FIRE_SIZE_CLASS', 'STAT_CAUSE_DESCR']).agg({'FOD_ID': 'count'})
    Petitfeu_pcts = PetitfeuCause.groupby(level=0).apply(lambda x:
                                                 100 * x / x.sum()).rename({'FOD_ID': 'count'}, axis=1).reset_index()
    fig13 = px.bar(Petitfeu_pcts, x="FIRE_SIZE_CLASS", y="count", color="STAT_CAUSE_DESCR", title="Causes des incendies pour les petits feux",labels={"FIRE_SIZE_CLASS":"Classe de taille", "count":"Nombre d'incendies"},height=500, width=600)
    fig13.update_layout(legend_title_text='Cause des feux')
    st.plotly_chart(fig13, use_container_width=True)

    Grand_petitfeuCause = df.groupby(['grand_ou_petit', 'STAT_CAUSE_DESCR']).agg({'FOD_ID': 'count'})
    Grand_petitfeu_pcts = Grand_petitfeuCause.groupby(level=0).apply(lambda x:
                                                 100 * x / x.sum()).rename({'FOD_ID': 'count'}, axis=1).reset_index()
    fig13b = px.bar(Grand_petitfeu_pcts, x="grand_ou_petit", y="count", color="STAT_CAUSE_DESCR", title="Comparaison des causes entre les petits et les grands feux",labels={"grand_ou_petit":"Taille du feu", "count":"Nombre d'incendies"},height=500, width=600)
    fig13b.update_layout(legend_title_text='Cause des feux')
    st.plotly_chart(fig13b, use_container_width=True)

    st.write("On peut voir que les débris en combustion représentent un part importante des feux de petite taille et que la foudre est à l'origine d'une grande partie des grands feux.")
    st.write(" ")
    st.markdown("---")
    st.write(" ")
    
    st.write("**Carte représentant les feux de plus de 100 acres en fonction de la cause de l'incendie**")
    st.write("Séléctionner les causes qui vous intéresse en cliquant sur son nom dans la légende.")
    dfmap4=Grandfeu.sort_values('FIRE_SIZE_CLASS')
    fig_map4 = px.scatter_mapbox(dfmap4,
                                  lat="LATITUDE",
                                  lon="LONGITUDE",
                                  color="STAT_CAUSE_DESCR",                       
                                  zoom=3,
                                  mapbox_style="open-street-map",
                                  width=1000,
                                  height=600)
    fig_map4.update_layout(legend_title_text='Cause des feux')
    fig_map4.update_traces(visible='legendonly') 

    st.plotly_chart(fig_map4, use_container_width=True)
    
    st.write(" ")
   
  #############################################################################################################################""
elif themes == "Machine learning": 
     st.markdown("<h1 style='text-align: center; color: blue;'>Peut-on prédire la classe de taille des feux à venir?</h1>", unsafe_allow_html=True)     

     st.write("")
     image = Image.open(r"C:\Users\thoma\Data\firemen3.JPG")
     st.image(image, caption=None)
     st.write(" ")
     st.write("Dans une optique de mise en situation, nous avons mis en place un algorithme de machine learning afin d'essayer de déterminer la classe de taille des futurs incendies pour pouvoir intervenir en conséquence.")
     st.write("Nous avons dans un premier temps essayé de déterminer la classe de taille de l'incendie (allant de la classe A à F soit de 0 à 5000+ acres.")
     st.markdown("---")
     
     st.write("Quel est le score de notre algorithme permettant de déterminer la classe de taille des incendies?")
     score = 0.5496619187275488
     score2 = 0.9717144429702228
     if st.button('Score'):
         st.write(score)
         st.write(" ")
         st.write("Le score de notre algorithme n'est pas très élevé.")
     st.write(" ")
     st.write(" ")
     st.write("Toujours dans cette optique de limiter l'impact des feux de forêt sur l'environnement et en espérant améliorer la prédiction de notre algorithme, peut-on prédire les feux de plus de 100 acres (environ 0.45 km2)?")
     if st.button('Score grand incendies'):
         st.write(score2)
    
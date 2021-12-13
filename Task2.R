library(dplyr)
library(ggplot2)

df <- read.csv(file = 'output_db.csv') %>% as_data_frame()
df_groupby = df %>% group_by(Year)
year_mov = df_groupby %>% summarise(Count = n()) %>%
  arrange(desc(Year), desc(Count))

ggplot(year_mov[1:21,], aes(Year, Count)) + 
  geom_bar(stat="identity", color='skyblue',fill='steelblue')+
  ggtitle("Yearly movies count") + 
  theme(axis.text.x=element_text(angle=45, hjust=1))

df_groupby = df %>% group_by(Country)
country_mov = df_groupby %>% summarise(Count = n()) %>%
  arrange(desc(Count))
       
ggplot(country_mov[1:11,], aes(reorder(Country,-Count), Count)) + 
  geom_bar(stat="identity", color='skyblue',fill='steelblue')+
  ggtitle("Countries movies count") + 
  theme(axis.text.x=element_text(angle=45, hjust=1))

df_groupby = df %>% group_by(imdbRating)
imdb_mov = df_groupby %>% summarise(Count = n()) %>%
  arrange(desc(Count))

ggplot(imdb_mov[2:56,],aes(imdbRating , Count)) + 
  geom_bar(stat="identity", color='skyblue',fill='steelblue')+
  ggtitle("Imdb Ratings") + 
  theme(axis.text.x=element_text(angle=45, hjust=1))

df_groupby = df %>% group_by(Genre)
genre_mov = df_groupby %>% summarise(Count = n()) %>%
  arrange(desc(Count))

ggplot(genre_mov[1:22,], aes(reorder(Genre,-Count), Count)) + 
  geom_bar(stat="identity", color='skyblue',fill='steelblue')+
  ggtitle("Genre movies count") + 
  theme(axis.text.x=element_text(angle=45, hjust=1))

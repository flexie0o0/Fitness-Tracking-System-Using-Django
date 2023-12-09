import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(layout="wide")

def recommend(video, cosine_sim, videos):
    indices = pd.Series(videos.index, index=videos['title'])
    idx = indices.get(video)
    
    if idx is None:
        print(f"Video '{video}' not found in the dataset.")
        return []

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    
    recommend_videos = []
    for i in sim_scores:
        work_id = i[0]
        try:
            video_info = videos.iloc[work_id]
            recommend_videos.append(video_info)
        except IndexError:
            print(f"IndexError: work_id={work_id}, len(videos)={len(videos)}")

    return recommend_videos

# Load the CSV file
videos = pd.read_csv(r'C:\Users\shinb\OneDrive\Documents\S_drive\Latestfile.CSV')  # Adjust the file path accordingly

videos = videos.drop_duplicates(subset='title')
# Load the pickle file
script_dir = os.path.dirname(os.path.abspath(__file__))
pkl_path = os.path.join(script_dir, 'similarity_latest.pkl')
cosine_sim = pickle.load(open(pkl_path, 'rb'))

# st.title('Workout Recommendation')
st.markdown("<h1 style='text-align: center;'>Workout Recommendation</h1>", unsafe_allow_html=True)

selected_workout_name = st.selectbox(
    'What do you wanna do today?',
    videos['title'].values
)



if st.button('Recommend'):
    recommendations = recommend(selected_workout_name, cosine_sim, videos)
    for video_info in recommendations:
        st.markdown(f"<h2 style='margin-bottom:8px;'>{video_info['title']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:20px;margin-bottom:20px;'>Description: {video_info['description']}</p>", unsafe_allow_html=True)

        # Display front and side videos side by side with increased size
        col1, col2 = st.columns(2)
        with col1:
            st.video(video_info['video_url'], format='video/mp4', start_time=0)
        with col2:
            st.video(video_info['side_video'], format='video/mp4', start_time=0)

        # Add space between videos
        st.markdown("<br><br>", unsafe_allow_html=True)






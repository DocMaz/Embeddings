import numpy as np
import plotly.graph_objects as go

# Define the sentence and words
sentence = "My dog stole my pizza."
words = sentence.split()

# Generate random 3D embeddings for each word
np.random.seed(42)  # For reproducibility
embeddings = {word: np.random.rand(3) for word in words}

# Extract coordinates for plotting
xs = [embeddings[word][0] for word in words]
ys = [embeddings[word][1] for word in words]
zs = [embeddings[word][2] for word in words]

# Create a 3D scatter plot with Plotly
fig = go.Figure(data=[go.Scatter3d(
    x=xs,
    y=ys,
    z=zs,
    mode='markers+text',
    text=words,
    textposition='top center',
    marker=dict(
        size=10,
        color='rgba(152, 0, 0, .8)',
        line=dict(
            width=2,
            color='rgba(255, 255, 255, .8)'
        )
    )
)])

# Set plot labels and title
fig.update_layout(
    title='3D Visualization of Sentence Embeddings',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    )
)

# Show plot
fig.show()

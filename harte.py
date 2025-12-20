import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from skimage import measure

def draw_professional_heart():
    """Renders a solid 3D heart using Marching Cubes."""
    # Setup the grid
    resolution = 100
    x = np.linspace(-1.5, 1.5, resolution)
    y = np.linspace(-1.5, 1.5, resolution)
    z = np.linspace(-1.5, 1.5, resolution)
    X, Y, Z = np.meshgrid(x, y, z)

    # Heart equation
    # F(x,y,z) = (x^2 + 9/4 y^2 + z^2 - 1)^3 - x^2 z^3 - 9/80 y^2 z^3
    # We want F(x,y,z) = 0
    
    F = (X**2 + (9/4)*Y**2 + Z**2 - 1)**3 - X**2 * Z**3 - (9/80) * Y**2 * Z**3

    # Marching cubes to find the surface mesh
    # level=0 extracts the isosurface where F=0
    verts, faces, normals, values = measure.marching_cubes(F, level=0, spacing=(x[1]-x[0], y[1]-y[0], z[1]-z[0]))

    # Center the mesh (since marching cubes returns indices-based coordinates scaled by spacing, but offset start needs correction if we want true coords)
    # Actually 'verts' from marching_cubes with spacing argument are relative to the grid origin if not careful, 
    # but let's just re-center based on our bounding box logic or use the raw indices and map back.
    # The 'verts' are returned in spatial coordinates if 'spacing' is provided, but it assumes start at (0,0,0).
    # We need to shift them back to our -1.5 range.
    
    verts[:, 0] += -1.5
    verts[:, 1] += -1.5
    verts[:, 2] += -1.5

    # Create the plot
    fig = plt.figure(figsize=(10, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # Create the mesh collection
    mesh = Poly3DCollection(verts[faces], alpha=0.9)
    mesh.set_facecolor('crimson')
    mesh.set_edgecolor('darkred')
    mesh.set_linewidth(0.1) # Thin lines for better definition

    ax.add_collection3d(mesh)

    # Set visualization limits
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(-1.5, 1.5)

    # Clean up axes for professional look
    ax.grid(False)
    ax.axis('off')
    
    # Lighting adjust (simple view init)
    ax.view_init(elev=30, azim=45)

    plt.title("Professional 3D Heart", color='white', fontsize=20, fontname='sans-serif')
    print("Displaying professional 3D heart. Close window to exit.")
    plt.show()

if __name__ == "__main__":
    draw_professional_heart()

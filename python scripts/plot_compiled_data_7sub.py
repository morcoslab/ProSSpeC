import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_paired_bar_chart(excel_file):
    """
    Create a paired bar chart from an Excel file with error bars.
    
    Parameters:
    -----------
    excel_file : str
        Path to the Excel file containing the data
    """
    try:
        # Read the Excel file, specifically the "Normalized" sheet
        df = pd.read_excel(excel_file, sheet_name="Normalized")
        
        # Extract the required columns
        enzymes = df["Enzyme"]
        with_enzyme = df["Normalized \"Enzyme\""]
        with_enzyme_error = df["Normalized Error with Enzyme"]
        no_enzyme = df["Normalized \"No Enzyme\""]
        no_enzyme_error = df["Normalized Error with no Enzyme"]
        
        # Set up the figure and axis
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Set width of bars
        bar_width = 0.35
        
        # Set positions of the bars on X axis
        x_pos = np.arange(len(enzymes))
        
        # Create bars
        ax.bar(x_pos - bar_width/2, with_enzyme, bar_width, 
               yerr=with_enzyme_error, label='With Enzyme', 
               capsize=5, alpha=0.8, color='blue')
        
        ax.bar(x_pos + bar_width/2, no_enzyme, bar_width, 
               yerr=no_enzyme_error, label='No Enzyme', 
               capsize=5, alpha=0.8, color='orange')
        
        # Add labels, title and legend with increased font sizes
        ax.set_xlabel('Enzyme with natural substrate', fontsize=16)
        ax.set_ylabel('sfCherryRFP (a.u.)', fontsize=16)
        ax.set_title('Normalized fluorescence reconstitution after splitting', fontsize=18, fontweight='bold')
        ax.set_ylim(0, 60)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(enzymes, rotation=45, ha='right', fontsize=12)
        ax.tick_params(axis='y', labelsize=14)
        ax.legend(fontsize=14)
        
        # Add grid for better readability
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Reduce empty space before and after the bars
        plt.xlim(x_pos[0] - bar_width - 0.2, x_pos[-1] + bar_width + 0.2)
        
        # Adjust layout to make room for the rotated x-axis labels
        plt.tight_layout()
        
        # Save the figure
        output_file = excel_file.rsplit('.', 1)[0] + '_bar_chart.png'
        plt.savefig(output_file, dpi=300)
        print(f"Bar chart saved as {output_file}")
        
        # Show the plot
        plt.show()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    excel_file = "/home/ceziegler/Documents/NIA_files/Compiled Data 20240222.xlsx"
    create_paired_bar_chart(excel_file)

""""""  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	 	 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	 	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 		  		  		    	 		 		   		 		  
or edited.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	 	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	 	 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt
import os

def author():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return "tb34"  # replace tb34 with your Georgia Tech username.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  

def study_group():
    """
    :return: A comma separated string of GT_Name of each member of your study group
    :rtype: str
    """
    return "tb34"

def gtid():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return 900897987  # replace with your GT ID number  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    result = False  		  	   		 	 	 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		 	 	 		  		  		    	 		 		   		 		  
        result = True  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return result  		  	   		 	 	 		  		  		    	 		 		   		 		  


def simulate_episode(win_prob, bankroll=None):
    """
    Simulate one episode of the martingale betting strategy
    
    :param win_prob: Probability of winning each spin
    :param bankroll: Maximum bankroll (None for unlimited)
    :return: Array of winnings for each spin (1001 elements including initial 0)
    """
    winnings = [0]  # Start with 0 winnings
    episode_winnings = 0
    bet_amount = 1
    
    for spin in range(1000):
        # Check if we've already won $80 or more
        if episode_winnings >= 80:
            winnings.append(episode_winnings)
            continue
            
        # Check if we've lost all our money (bankroll constraint)
        if bankroll is not None and episode_winnings <= -bankroll:
            winnings.append(-bankroll)
            continue
            
        # Adjust bet if bankroll constraint would be violated
        if bankroll is not None and episode_winnings - bet_amount < -bankroll:
            bet_amount = bankroll + episode_winnings
            
        # If we can't bet anything, we're done
        if bet_amount <= 0:
            winnings.append(episode_winnings)
            continue
            
        # Spin the wheel
        won = get_spin_result(win_prob)
        
        if won:
            episode_winnings += bet_amount
            bet_amount = 1  # Reset bet amount after winning
        else:
            episode_winnings -= bet_amount
            bet_amount *= 2  # Double the bet after losing
            
        winnings.append(episode_winnings)
        
        # If we won $80 or more, we're done betting
        if episode_winnings >= 80:
            continue
    
    return np.array(winnings)


def experiment_1():
    """
    Run Experiment 1: Unlimited bankroll
    """
    # American roulette probability: 18 black slots out of 38 total
    win_prob = 18.0/38.0
    
    # Figure 1: 10 episodes
    episodes_10 = []
    for i in range(10):
        episode_data = simulate_episode(win_prob)
        episodes_10.append(episode_data)
    
    # Plot Figure 1
    plt.figure(figsize=(10, 6))
    for i, episode in enumerate(episodes_10):
        plt.plot(range(len(episode)), episode, label=f'Episode {i+1}')
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.title('Figure 1: 10 Episodes of Martingale Strategy (Unlimited Bankroll)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
    
    plt.savefig('images/figure1.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Run 1000 episodes for Figures 2 and 3
    episodes_1000 = []
    for i in range(1000):
        episode_data = simulate_episode(win_prob)
        episodes_1000.append(episode_data)
    
    # Convert to numpy array for easier manipulation
    episodes_array = np.array(episodes_1000)
    
    # Calculate statistics
    mean_winnings = np.mean(episodes_array, axis=0)
    std_winnings = np.std(episodes_array, axis=0, ddof=0)  # Population standard deviation
    median_winnings = np.median(episodes_array, axis=0)
    
    # Figure 2: Mean with standard deviation
    plt.figure(figsize=(10, 6))
    x = range(len(mean_winnings))
    plt.plot(x, mean_winnings, label='Mean', color='blue')
    plt.plot(x, mean_winnings + std_winnings, label='Mean + Std Dev', color='red', linestyle='--')
    plt.plot(x, mean_winnings - std_winnings, label='Mean - Std Dev', color='red', linestyle='--')
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.title('Figure 2: Mean Winnings with Standard Deviation (1000 Episodes, Unlimited Bankroll)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('images/figure2.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Figure 3: Median with standard deviation
    plt.figure(figsize=(10, 6))
    plt.plot(x, median_winnings, label='Median', color='green')
    plt.plot(x, median_winnings + std_winnings, label='Median + Std Dev', color='orange', linestyle='--')
    plt.plot(x, median_winnings - std_winnings, label='Median - Std Dev', color='orange', linestyle='--')
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.title('Figure 3: Median Winnings with Standard Deviation (1000 Episodes, Unlimited Bankroll)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('images/figure3.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return episodes_array


def experiment_2():
    """
    Run Experiment 2: Limited bankroll ($256)
    """
    # American roulette probability: 18 black slots out of 38 total
    win_prob = 18.0/38.0
    bankroll = 256
    
    # Run 1000 episodes
    episodes_1000 = []
    for i in range(1000):
        episode_data = simulate_episode(win_prob, bankroll)
        episodes_1000.append(episode_data)
    
    # Convert to numpy array
    episodes_array = np.array(episodes_1000)
    
    # Calculate statistics
    mean_winnings = np.mean(episodes_array, axis=0)
    std_winnings = np.std(episodes_array, axis=0, ddof=0)  # Population standard deviation
    median_winnings = np.median(episodes_array, axis=0)
    
    # Figure 4: Mean with standard deviation (realistic simulator)
    plt.figure(figsize=(10, 6))
    x = range(len(mean_winnings))
    plt.plot(x, mean_winnings, label='Mean', color='blue')
    plt.plot(x, mean_winnings + std_winnings, label='Mean + Std Dev', color='red', linestyle='--')
    plt.plot(x, mean_winnings - std_winnings, label='Mean - Std Dev', color='red', linestyle='--')
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.title('Figure 4: Mean Winnings with Standard Deviation (1000 Episodes, $256 Bankroll)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('images/figure4.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Figure 5: Median with standard deviation (realistic simulator)
    plt.figure(figsize=(10, 6))
    plt.plot(x, median_winnings, label='Median', color='green')
    plt.plot(x, median_winnings + std_winnings, label='Median + Std Dev', color='orange', linestyle='--')
    plt.plot(x, median_winnings - std_winnings, label='Median - Std Dev', color='orange', linestyle='--')
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings ($)')
    plt.title('Figure 5: Median Winnings with Standard Deviation (1000 Episodes, $256 Bankroll)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('images/figure5.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return episodes_array


def test_code():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    win_prob = 18.0/38.0  # American roulette probability for black
    np.random.seed(gtid())  # do this only once  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Test spin result: {get_spin_result(win_prob)}")  # test the roulette spin  		  	   		 	 	 		  		  		    	 		 		   		 		  
    
    print("Running Experiment 1...")
    exp1_results = experiment_1()
    
    print("Running Experiment 2...")
    exp2_results = experiment_2()
    
    # Calculate and print some statistics for the report
    print("\n=== EXPERIMENT 1 RESULTS (Unlimited Bankroll) ===")
    # Probability of winning exactly $80
    wins_80_exp1 = np.sum(exp1_results[:, -1] >= 80)
    prob_win_80_exp1 = wins_80_exp1 / 1000.0
    print(f"Probability of winning $80 or more: {prob_win_80_exp1:.4f}")
    
    # Expected value after 1000 bets
    expected_value_exp1 = np.mean(exp1_results[:, -1])
    print(f"Expected value after 1000 bets: ${expected_value_exp1:.2f}")
    
    print("\n=== EXPERIMENT 2 RESULTS (Limited Bankroll) ===")
    # Probability of winning exactly $80
    wins_80_exp2 = np.sum(exp2_results[:, -1] >= 80)
    prob_win_80_exp2 = wins_80_exp2 / 1000.0
    print(f"Probability of winning $80 or more: {prob_win_80_exp2:.4f}")
    
    # Expected value after 1000 bets
    expected_value_exp2 = np.mean(exp2_results[:, -1])
    print(f"Expected value after 1000 bets: ${expected_value_exp2:.2f}")
    
    print("\nAll figures saved to images/ directory")
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		 	 	 		  		  		    	 		 		   		 		  
    test_code()
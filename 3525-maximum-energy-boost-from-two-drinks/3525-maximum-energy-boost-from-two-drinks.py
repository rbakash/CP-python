class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        dpA=[0]*len(energyDrinkA)
        dpB=[0]*len(energyDrinkA)
        dpA[0]=energyDrinkA[0]
        dpB[0]=energyDrinkB[0]

        for index in range(1, len(energyDrinkA)):
            # consider first drink or second last drink in energy Drink B 
            dpA[index]=energyDrinkA[index] + max(dpA[index-1],dpB[index-2] if index >=2 else 0)
            dpB[index]=energyDrinkB[index] + max(dpB[index-1],dpA[index-2] if index >=2 else 0)

        return max(dpA[-1],dpB[-1])
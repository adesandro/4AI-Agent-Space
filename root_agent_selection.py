class RootAgent:
    def __init__(self, agent_cluster):
        self.cluster = agent_cluster # A list of registered agent objects

    def select_best_agent(self, task_tags):
        """
        Finds the highest rated agent that possesses ALL required tags.
        """
        eligible_agents = []

        for agent in self.cluster:
            # Check if the agent's tags are a superset of the task requirements
            if set(task_tags).issubset(set(agent['tag'])):
                eligible_agents.append(agent)

        if not eligible_agents:
            return None

        # Sort by rating (highest first) and return the winner
        # Note: Rating is a value 1.0 - 5.0 updated by the evaluation phase
        winner = max(eligible_agents, key=lambda x: x.get('rating', 0))
        return winner

# Example Cluster Data
agent_cluster = [
    {"name": "Agent A", "tag": [1, 3, 4], "rating": 4.8, "url": "https://4ai.agent/a"},
    {"name": "Agent B", "tag": [1, 4], "rating": 4.2, "url": "https://4ai.agent/b"},
    {"name": "Agent C", "tag": [1, 3, 4], "rating": 3.5, "url": "https://4ai.agent/c"}
]

# Pioneer sends a task with Tags {1, 4}
master = RootAgent(agent_cluster)
best_choice = master.select_best_agent([1, 4])

print(f"Root Agent selected: {best_choice['name']} with rating {best_choice['rating']}")

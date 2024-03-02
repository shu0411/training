int heroHealth = 10;
int monsterHealth = 10;
int currentHealth = 0;
Random random = new Random();
string currentTarget = "Monster";

do
{
    if (currentTarget.Equals("Monster"))
    {
        currentHealth = monsterHealth;
    }
    else
    {
        currentHealth = heroHealth;
    }

    // Attack
    int damage = random.Next(1, 11);
    currentHealth -= damage;    
    Console.WriteLine($"{currentTarget} was damaged and lost {damage} health and now has {currentHealth} health.");

    if (currentTarget.Equals("Monster"))
    {
        monsterHealth = currentHealth;
        currentTarget = "Hero";
    }
    else
    {
        heroHealth = currentHealth;
        currentTarget = "Monster";
    }
}
while (heroHealth > 0 && monsterHealth > 0);

Console.WriteLine($"{currentTarget} wins!");
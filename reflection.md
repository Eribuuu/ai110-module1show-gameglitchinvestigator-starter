# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game visually looked fine when I first ran it. The bugs that I noticed right off the bat was that the hints were backwards
(such as saying to go higher when you inputted a number higher than the target number), Also that the ranges were flipped for Normal and Hard difficulties. Two other bugs that I found when interacting with the app was that the new game button didnt work as intended (only updating the target number) and inputting nothing and hitting submit guess allowed for the guess count to go past the amount given for the given difficulty.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used claude since it can be used within VS Code along side my editor. One example of the AI being right was when it changed the ranges for the difficulties. I verfied it by looking at the code it had produced (this was a pretty simple function and easy to see how each branch returned the set values). One instance where the AI was wrong was when I left in FIXME above a function during the refactor to the logic_util file. The chanegs it proposed was to revert the logic in get_range_for_difficulty back to its buggy state and I was able to catch that it had reverted the changes during the move by reviewing the diffs before accepting the changes for the refactor.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Most of the logic that had bugs in it and was fixed was tested by going back to the UI and seeing if the intended functionality was
present. One test I did was to see if the hints were correct so I submitted guesses where I knew what the ourtcome should be (i.e the target number is 18 but I guessed 20 to see if it says to guess lower). AI helped create the tests for pytest and that was because of the assignment requirement but the design of the tests was something that I had told it to implement, basically testing each branch of the function.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

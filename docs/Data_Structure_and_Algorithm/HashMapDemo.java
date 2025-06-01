import java.util.HashMap;
import java.util.Set;
/**
 * HashMap<K,V> is a generic class where:
 * K - the type of keys maintained by this map
 * V - the type of mapped values
 */
public class HashMapDemo {
    public static void main(String[] args) {
        // Create HashMap
        HashMap<String, Integer> studentScores = new HashMap<>();

        // Basic put method
        studentScores.put("Alice", 95);  // Add new entry
        studentScores.put("Bob", 88);
        System.out.println("After putting Alice and Bob: " + studentScores);
        String[] names = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"};
        int[] scores = {95, 88, 75, 90, 85, 92, 88, 95, 80, 90};
        for (int i = 0; i < names.length; i++) {
            studentScores.put(names[i], scores[i]);
        }
        System.out.println("Student scores: " + studentScores);

        // Create a new HashMap with existing data
        HashMap<String, Integer> existingMap = new HashMap<>();
        existingMap.put("A", 1);
        existingMap.put("B", 2);
        HashMap<String, Integer> map4 = new HashMap<>(existingMap);
        map4.put("C", 3);
        System.out.println("map4: " + map4);


        // put returns the previous value
        Integer oldValue = studentScores.put("Alice", 97);  // Update existing entry
        System.out.println("Alice's old score was: " + oldValue);
        System.out.println("After updating Alice: " + studentScores);

        // containsKey check
        String checkName = "Charlie";
        if (studentScores.containsKey(checkName)) {
            System.out.println(checkName + " exists in the map");
        } else {
            System.out.println(checkName + " does not exist in the map");
        }

        // replace method
        // Replace only if key exists
        boolean replaced = studentScores.replace("Bob", 88, 90);
        System.out.println("Was Bob's score replaced? " + replaced);
        System.out.println("Bob's new score: " + studentScores.get("Bob"));

        // Try to replace non-existent key
        boolean notReplaced = studentScores.replace("Charlie", 85, 90);
        System.out.println("Was Charlie's score replaced? " + notReplaced);

        // Simple replace (just update value)
        studentScores.replace("Alice", 100);
        System.out.println("Alice's final score: " + studentScores.get("Alice"));



        // Iterate using keySet
        Set<String> keys = studentScores.keySet();
        System.out.println("studentScores.entrySet(): " + studentScores.entrySet());
        // for(String key : studentScores.keySet()) {
        //     System.out.println(key + ": " + studentScores.get(key));
        // }

        // Method 1: Using for-each loop
        for (String key : keys) {
            System.out.println(key + ": " + studentScores.get(key));
        }
        
        // Method 2: Using forEach with lambda
        System.out.println("\nMethod 2: Using forEach with lambda");
        keys.forEach(key -> System.out.println(key + ": " + studentScores.get(key)));
        // parameter -> expression
        // }
        
        // Method 3: Using iterator
        var iterator = keys.iterator();
        while (iterator.hasNext()) {
            String key = iterator.next();
            System.out.println(key + ": " + studentScores.get(key));
        }

        // Clear HashMap
        studentScores.clear();
        System.out.println("\nNumber of students after clearing: " + studentScores.size());
    }
} 
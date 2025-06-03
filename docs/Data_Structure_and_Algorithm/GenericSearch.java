/**
 * This class demonstrates generic linear search implementation in Java.
 * It shows two different approaches to implementing a generic linear search:
 * 1. A static method approach (GenericLinearSearchMethod)
 * 2. A class-based approach (GenericLinearSearchClass)
 * @author Yupeng Yang
 * @version Jun 02, 2025
 */

public class GenericSearch {

    public static class GenericLinearSearchMethod {
        public static <T> int linearSearch(T[] arr, T target) {
            for (int i = 0; i < arr.length; i++) {
                if (arr[i].equals(target)) {
                    return i;
                }
            }
            return -1;
        }
    }

    public static class GenericLinearSearchClass<T> {
        private T[] array;
    
        public GenericLinearSearchClass(T[] array) {
            this.array = array;
        }
    
        public int linearSearch(T target) {
            for (int i = 0; i < array.length; i++) {
                if (array[i].equals(target)) {
                    return i;
                }
            }
            return -1;
        }
    }

    public static void main(String[] args) {
        Integer[] array1 = {1, 2, 3, 4, 5};
        Integer target1 = 1;
        String[] array2 = {"apple", "banana", "cherry", "date", "elderberry"};
        String target2 = "cherry";

        System.out.println(GenericLinearSearchMethod.linearSearch(array1, target1)); 
        System.out.println(GenericLinearSearchMethod.linearSearch(array2, target2));

        System.out.println("--------------------------------");

        GenericLinearSearchClass<Integer> search = new GenericLinearSearchClass<>(array1);
        System.out.println(search.linearSearch(target1));
        GenericLinearSearchClass<String> search2 = new GenericLinearSearchClass<>(array2);
        System.out.println(search2.linearSearch(target2));    
    }
}
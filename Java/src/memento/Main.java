// memento pattern is used to store the state of an object
// so that it can be restored later on.
// It is one of the behavioral design patterns.
package memento;

public class Main {
    public static void main(String[] args) {
        Editor editor;
        editor = new Editor();
        editor.setContent("a");
        editor.setContent("b");
        editor.setContent("c");
//        editor.undo();
    }
}

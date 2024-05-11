package memento;

public class EditorState {
    // final means that the value of the variable cannot be changed
    private final string content;

    
    public EditorState(string content) {
        this.content = content;
    }

    public string getContent() {
        return content;
    }
}

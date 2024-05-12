// state pattern is used to change the behavior of an object when its internal state changes.
// It is one of the behavioral design patterns.

package state;

public class Canvas {
    private Tool currentTool;

    public void mouseDown(){
        currentTool.mouseDown();
    }

    public void mouseUp(){
        currentTool.mouseUp();
    }

    public Tool getCurrentTool() {
        return currentTool;
    }

    public void setCurrentTool(Tool currentTool) {
        this.currentTool = currentTool;
    }
}

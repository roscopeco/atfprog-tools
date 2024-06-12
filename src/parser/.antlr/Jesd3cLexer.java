// Generated from /Users/rosco/Development/electronics/atf15xxprog/atfprog-tools/src/parser/Jesd3cLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class Jesd3cLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		STX=1, ETX=2, TERMINATOR=3, NOTE_ID=4, FUSE_LIST_ID=5, DIGIT=6, HEX_DIGIT=7, 
		BINARY_DIGIT=8, BINARY_NUMBER=9, NUMBER=10, SPACE=11, NOTE=12, NOTE_TERM=13;
	public static final int
		NOTE_MODE=1;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "NOTE_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"STX", "ETX", "TERMINATOR", "NOTE_ID", "FUSE_LIST_ID", "DIGIT", "HEX_DIGIT", 
			"BINARY_DIGIT", "BINARY_NUMBER", "NUMBER", "SPACE", "NOTE", "NOTE_TERM"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\u0002'", "'\\u0003'", null, null, "'L'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "STX", "ETX", "TERMINATOR", "NOTE_ID", "FUSE_LIST_ID", "DIGIT", 
			"HEX_DIGIT", "BINARY_DIGIT", "BINARY_NUMBER", "NUMBER", "SPACE", "NOTE", 
			"NOTE_TERM"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public Jesd3cLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Jesd3cLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\rO\u0006\uffff\uffff\u0006\uffff\uffff\u0002\u0000\u0007"+
		"\u0000\u0002\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007"+
		"\u0003\u0002\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007"+
		"\u0006\u0002\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n"+
		"\u0007\n\u0002\u000b\u0007\u000b\u0002\f\u0007\f\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003\'\b\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0003\u00061\b\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0005\b"+
		"7\b\b\n\b\f\b:\t\b\u0001\t\u0001\t\u0005\t>\b\t\n\t\f\tA\t\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0004\u000bH\b\u000b\u000b\u000b\f\u000b"+
		"I\u0001\f\u0001\f\u0001\f\u0001\f\u0000\u0000\r\u0002\u0001\u0004\u0002"+
		"\u0006\u0003\b\u0004\n\u0005\f\u0006\u000e\u0007\u0010\b\u0012\t\u0014"+
		"\n\u0016\u000b\u0018\f\u001a\r\u0002\u0000\u0001\u0005\u0001\u000009\u0001"+
		"\u0000AF\u0001\u000001\u0003\u0000\t\n\r\r  \u0001\u0000**R\u0000\u0002"+
		"\u0001\u0000\u0000\u0000\u0000\u0004\u0001\u0000\u0000\u0000\u0000\u0006"+
		"\u0001\u0000\u0000\u0000\u0000\b\u0001\u0000\u0000\u0000\u0000\n\u0001"+
		"\u0000\u0000\u0000\u0000\f\u0001\u0000\u0000\u0000\u0000\u000e\u0001\u0000"+
		"\u0000\u0000\u0000\u0010\u0001\u0000\u0000\u0000\u0000\u0012\u0001\u0000"+
		"\u0000\u0000\u0000\u0014\u0001\u0000\u0000\u0000\u0000\u0016\u0001\u0000"+
		"\u0000\u0000\u0001\u0018\u0001\u0000\u0000\u0000\u0001\u001a\u0001\u0000"+
		"\u0000\u0000\u0002\u001c\u0001\u0000\u0000\u0000\u0004\u001e\u0001\u0000"+
		"\u0000\u0000\u0006 \u0001\u0000\u0000\u0000\b\"\u0001\u0000\u0000\u0000"+
		"\n*\u0001\u0000\u0000\u0000\f,\u0001\u0000\u0000\u0000\u000e0\u0001\u0000"+
		"\u0000\u0000\u00102\u0001\u0000\u0000\u0000\u00124\u0001\u0000\u0000\u0000"+
		"\u0014;\u0001\u0000\u0000\u0000\u0016B\u0001\u0000\u0000\u0000\u0018G"+
		"\u0001\u0000\u0000\u0000\u001aK\u0001\u0000\u0000\u0000\u001c\u001d\u0005"+
		"\u0002\u0000\u0000\u001d\u0003\u0001\u0000\u0000\u0000\u001e\u001f\u0005"+
		"\u0003\u0000\u0000\u001f\u0005\u0001\u0000\u0000\u0000 !\u0005*\u0000"+
		"\u0000!\u0007\u0001\u0000\u0000\u0000\"&\u0005N\u0000\u0000#$\u0005O\u0000"+
		"\u0000$%\u0005T\u0000\u0000%\'\u0005E\u0000\u0000&#\u0001\u0000\u0000"+
		"\u0000&\'\u0001\u0000\u0000\u0000\'(\u0001\u0000\u0000\u0000()\u0006\u0003"+
		"\u0000\u0000)\t\u0001\u0000\u0000\u0000*+\u0005L\u0000\u0000+\u000b\u0001"+
		"\u0000\u0000\u0000,-\u0007\u0000\u0000\u0000-\r\u0001\u0000\u0000\u0000"+
		".1\u0003\f\u0005\u0000/1\u0007\u0001\u0000\u00000.\u0001\u0000\u0000\u0000"+
		"0/\u0001\u0000\u0000\u00001\u000f\u0001\u0000\u0000\u000023\u0007\u0002"+
		"\u0000\u00003\u0011\u0001\u0000\u0000\u000048\u0003\u0010\u0007\u0000"+
		"57\u0003\u0010\u0007\u000065\u0001\u0000\u0000\u00007:\u0001\u0000\u0000"+
		"\u000086\u0001\u0000\u0000\u000089\u0001\u0000\u0000\u00009\u0013\u0001"+
		"\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000;?\u0003\f\u0005\u0000<>\u0003"+
		"\f\u0005\u0000=<\u0001\u0000\u0000\u0000>A\u0001\u0000\u0000\u0000?=\u0001"+
		"\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@\u0015\u0001\u0000\u0000"+
		"\u0000A?\u0001\u0000\u0000\u0000BC\u0007\u0003\u0000\u0000CD\u0001\u0000"+
		"\u0000\u0000DE\u0006\n\u0001\u0000E\u0017\u0001\u0000\u0000\u0000FH\b"+
		"\u0004\u0000\u0000GF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000"+
		"IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000J\u0019\u0001\u0000"+
		"\u0000\u0000KL\u0005*\u0000\u0000LM\u0001\u0000\u0000\u0000MN\u0006\f"+
		"\u0002\u0000N\u001b\u0001\u0000\u0000\u0000\u0007\u0000\u0001&08?I\u0003"+
		"\u0005\u0001\u0000\u0000\u0001\u0000\u0004\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
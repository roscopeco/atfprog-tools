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
		STX=1, ETX=2, TERMINATOR=3, NOTE_ID=4, FUSE_LIST_ID=5, HEX_DIGIT=6, BINARY_NUMBER=7, 
		NUMBER=8, SPACE=9, NOTE=10;
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
			"STX", "ETX", "TERMINATOR", "NOTE_ID", "FUSE_LIST_ID", "DIGIT", "BINARY_DIGIT", 
			"HEX_DIGIT", "BINARY_NUMBER", "NUMBER", "FIELD_CHARACTER", "SPACE", "NOTE", 
			"NOTE_TERM"
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
			null, "STX", "ETX", "TERMINATOR", "NOTE_ID", "FUSE_LIST_ID", "HEX_DIGIT", 
			"BINARY_NUMBER", "NUMBER", "SPACE", "NOTE"
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
		"\u0004\u0000\nV\u0006\uffff\uffff\u0006\uffff\uffff\u0002\u0000\u0007"+
		"\u0000\u0002\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007"+
		"\u0003\u0002\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007"+
		"\u0006\u0002\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n"+
		"\u0007\n\u0002\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003"+
		"\u0003+\b\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0003"+
		"\u00077\b\u0007\u0001\b\u0001\b\u0005\b;\b\b\n\b\f\b>\t\b\u0001\t\u0001"+
		"\t\u0005\tB\b\t\n\t\f\tE\t\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0004\fN\b\f\u000b\f\f\fO\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0000\u0000\u000e\u0002\u0001\u0004\u0002\u0006\u0003"+
		"\b\u0004\n\u0005\f\u0000\u000e\u0000\u0010\u0006\u0012\u0007\u0014\b\u0016"+
		"\u0000\u0018\t\u001a\n\u001c\u0000\u0002\u0000\u0001\u0005\u0001\u0000"+
		"09\u0001\u000001\u0001\u0000AF\u0002\u0000 )+~\u0003\u0000\t\n\r\r  V"+
		"\u0000\u0002\u0001\u0000\u0000\u0000\u0000\u0004\u0001\u0000\u0000\u0000"+
		"\u0000\u0006\u0001\u0000\u0000\u0000\u0000\b\u0001\u0000\u0000\u0000\u0000"+
		"\n\u0001\u0000\u0000\u0000\u0000\u0010\u0001\u0000\u0000\u0000\u0000\u0012"+
		"\u0001\u0000\u0000\u0000\u0000\u0014\u0001\u0000\u0000\u0000\u0000\u0018"+
		"\u0001\u0000\u0000\u0000\u0001\u001a\u0001\u0000\u0000\u0000\u0001\u001c"+
		"\u0001\u0000\u0000\u0000\u0002\u001e\u0001\u0000\u0000\u0000\u0004\"\u0001"+
		"\u0000\u0000\u0000\u0006$\u0001\u0000\u0000\u0000\b&\u0001\u0000\u0000"+
		"\u0000\n.\u0001\u0000\u0000\u0000\f0\u0001\u0000\u0000\u0000\u000e2\u0001"+
		"\u0000\u0000\u0000\u00106\u0001\u0000\u0000\u0000\u00128\u0001\u0000\u0000"+
		"\u0000\u0014?\u0001\u0000\u0000\u0000\u0016F\u0001\u0000\u0000\u0000\u0018"+
		"H\u0001\u0000\u0000\u0000\u001aM\u0001\u0000\u0000\u0000\u001cQ\u0001"+
		"\u0000\u0000\u0000\u001e\u001f\u0005\u0002\u0000\u0000\u001f \u0001\u0000"+
		"\u0000\u0000 !\u0006\u0000\u0000\u0000!\u0003\u0001\u0000\u0000\u0000"+
		"\"#\u0005\u0003\u0000\u0000#\u0005\u0001\u0000\u0000\u0000$%\u0005*\u0000"+
		"\u0000%\u0007\u0001\u0000\u0000\u0000&*\u0005N\u0000\u0000\'(\u0005O\u0000"+
		"\u0000()\u0005T\u0000\u0000)+\u0005E\u0000\u0000*\'\u0001\u0000\u0000"+
		"\u0000*+\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000,-\u0006\u0003"+
		"\u0000\u0000-\t\u0001\u0000\u0000\u0000./\u0005L\u0000\u0000/\u000b\u0001"+
		"\u0000\u0000\u000001\u0007\u0000\u0000\u00001\r\u0001\u0000\u0000\u0000"+
		"23\u0007\u0001\u0000\u00003\u000f\u0001\u0000\u0000\u000047\u0003\f\u0005"+
		"\u000057\u0007\u0002\u0000\u000064\u0001\u0000\u0000\u000065\u0001\u0000"+
		"\u0000\u00007\u0011\u0001\u0000\u0000\u00008<\u0003\u000e\u0006\u0000"+
		"9;\u0003\u000e\u0006\u0000:9\u0001\u0000\u0000\u0000;>\u0001\u0000\u0000"+
		"\u0000<:\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=\u0013\u0001"+
		"\u0000\u0000\u0000><\u0001\u0000\u0000\u0000?C\u0003\f\u0005\u0000@B\u0003"+
		"\f\u0005\u0000A@\u0001\u0000\u0000\u0000BE\u0001\u0000\u0000\u0000CA\u0001"+
		"\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000D\u0015\u0001\u0000\u0000"+
		"\u0000EC\u0001\u0000\u0000\u0000FG\u0007\u0003\u0000\u0000G\u0017\u0001"+
		"\u0000\u0000\u0000HI\u0007\u0004\u0000\u0000IJ\u0001\u0000\u0000\u0000"+
		"JK\u0006\u000b\u0001\u0000K\u0019\u0001\u0000\u0000\u0000LN\u0003\u0016"+
		"\n\u0000ML\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000OM\u0001\u0000"+
		"\u0000\u0000OP\u0001\u0000\u0000\u0000P\u001b\u0001\u0000\u0000\u0000"+
		"QR\u0005*\u0000\u0000RS\u0001\u0000\u0000\u0000ST\u0006\r\u0002\u0000"+
		"TU\u0006\r\u0003\u0000U\u001d\u0001\u0000\u0000\u0000\u0007\u0000\u0001"+
		"*6<CO\u0004\u0005\u0001\u0000\u0000\u0001\u0000\u0004\u0000\u0000\u0007"+
		"\u0003\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
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
		STX=1, ETX=2, TERMINATOR=3, NOTE_ID=4, VAL_FUS_ID=5, VAL_PIN_ID=6, VAL_VEC_ID=7, 
		FUSE_LIST_ID=8, HEX_DIGIT=9, BINARY_NUMBER=10, NUMBER=11, SPACE=12, NOTE=13;
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
			"STX", "ETX", "TERMINATOR", "NOTE_ID", "VAL_FUS_ID", "VAL_PIN_ID", "VAL_VEC_ID", 
			"FUSE_LIST_ID", "DIGIT", "BINARY_DIGIT", "HEX_DIGIT", "BINARY_NUMBER", 
			"NUMBER", "FIELD_CHARACTER", "SPACE", "NOTE", "NOTE_TERM"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\u0002'", "'\\u0003'", null, null, "'QF'", "'QP'", "'QV'", "'L'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "STX", "ETX", "TERMINATOR", "NOTE_ID", "VAL_FUS_ID", "VAL_PIN_ID", 
			"VAL_VEC_ID", "FUSE_LIST_ID", "HEX_DIGIT", "BINARY_NUMBER", "NUMBER", 
			"SPACE", "NOTE"
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
		"\u0004\u0000\re\u0006\uffff\uffff\u0006\uffff\uffff\u0002\u0000\u0007"+
		"\u0000\u0002\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007"+
		"\u0003\u0002\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007"+
		"\u0006\u0002\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n"+
		"\u0007\n\u0002\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002"+
		"\u000e\u0007\u000e\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003"+
		"\u00031\b\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n"+
		"\u0001\n\u0003\nF\b\n\u0001\u000b\u0001\u000b\u0005\u000bJ\b\u000b\n\u000b"+
		"\f\u000bM\t\u000b\u0001\f\u0001\f\u0005\fQ\b\f\n\f\f\fT\t\f\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0004\u000f"+
		"]\b\u000f\u000b\u000f\f\u000f^\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0000\u0000\u0011\u0002\u0001\u0004\u0002\u0006\u0003"+
		"\b\u0004\n\u0005\f\u0006\u000e\u0007\u0010\b\u0012\u0000\u0014\u0000\u0016"+
		"\t\u0018\n\u001a\u000b\u001c\u0000\u001e\f \r\"\u0000\u0002\u0000\u0001"+
		"\u0005\u0001\u000009\u0001\u000001\u0001\u0000AF\u0002\u0000 )+~\u0003"+
		"\u0000\t\n\r\r  e\u0000\u0002\u0001\u0000\u0000\u0000\u0000\u0004\u0001"+
		"\u0000\u0000\u0000\u0000\u0006\u0001\u0000\u0000\u0000\u0000\b\u0001\u0000"+
		"\u0000\u0000\u0000\n\u0001\u0000\u0000\u0000\u0000\f\u0001\u0000\u0000"+
		"\u0000\u0000\u000e\u0001\u0000\u0000\u0000\u0000\u0010\u0001\u0000\u0000"+
		"\u0000\u0000\u0016\u0001\u0000\u0000\u0000\u0000\u0018\u0001\u0000\u0000"+
		"\u0000\u0000\u001a\u0001\u0000\u0000\u0000\u0000\u001e\u0001\u0000\u0000"+
		"\u0000\u0001 \u0001\u0000\u0000\u0000\u0001\"\u0001\u0000\u0000\u0000"+
		"\u0002$\u0001\u0000\u0000\u0000\u0004(\u0001\u0000\u0000\u0000\u0006*"+
		"\u0001\u0000\u0000\u0000\b,\u0001\u0000\u0000\u0000\n4\u0001\u0000\u0000"+
		"\u0000\f7\u0001\u0000\u0000\u0000\u000e:\u0001\u0000\u0000\u0000\u0010"+
		"=\u0001\u0000\u0000\u0000\u0012?\u0001\u0000\u0000\u0000\u0014A\u0001"+
		"\u0000\u0000\u0000\u0016E\u0001\u0000\u0000\u0000\u0018G\u0001\u0000\u0000"+
		"\u0000\u001aN\u0001\u0000\u0000\u0000\u001cU\u0001\u0000\u0000\u0000\u001e"+
		"W\u0001\u0000\u0000\u0000 \\\u0001\u0000\u0000\u0000\"`\u0001\u0000\u0000"+
		"\u0000$%\u0005\u0002\u0000\u0000%&\u0001\u0000\u0000\u0000&\'\u0006\u0000"+
		"\u0000\u0000\'\u0003\u0001\u0000\u0000\u0000()\u0005\u0003\u0000\u0000"+
		")\u0005\u0001\u0000\u0000\u0000*+\u0005*\u0000\u0000+\u0007\u0001\u0000"+
		"\u0000\u0000,0\u0005N\u0000\u0000-.\u0005O\u0000\u0000./\u0005T\u0000"+
		"\u0000/1\u0005E\u0000\u00000-\u0001\u0000\u0000\u000001\u0001\u0000\u0000"+
		"\u000012\u0001\u0000\u0000\u000023\u0006\u0003\u0000\u00003\t\u0001\u0000"+
		"\u0000\u000045\u0005Q\u0000\u000056\u0005F\u0000\u00006\u000b\u0001\u0000"+
		"\u0000\u000078\u0005Q\u0000\u000089\u0005P\u0000\u00009\r\u0001\u0000"+
		"\u0000\u0000:;\u0005Q\u0000\u0000;<\u0005V\u0000\u0000<\u000f\u0001\u0000"+
		"\u0000\u0000=>\u0005L\u0000\u0000>\u0011\u0001\u0000\u0000\u0000?@\u0007"+
		"\u0000\u0000\u0000@\u0013\u0001\u0000\u0000\u0000AB\u0007\u0001\u0000"+
		"\u0000B\u0015\u0001\u0000\u0000\u0000CF\u0003\u0012\b\u0000DF\u0007\u0002"+
		"\u0000\u0000EC\u0001\u0000\u0000\u0000ED\u0001\u0000\u0000\u0000F\u0017"+
		"\u0001\u0000\u0000\u0000GK\u0003\u0014\t\u0000HJ\u0003\u0014\t\u0000I"+
		"H\u0001\u0000\u0000\u0000JM\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000"+
		"\u0000KL\u0001\u0000\u0000\u0000L\u0019\u0001\u0000\u0000\u0000MK\u0001"+
		"\u0000\u0000\u0000NR\u0003\u0012\b\u0000OQ\u0003\u0012\b\u0000PO\u0001"+
		"\u0000\u0000\u0000QT\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000"+
		"RS\u0001\u0000\u0000\u0000S\u001b\u0001\u0000\u0000\u0000TR\u0001\u0000"+
		"\u0000\u0000UV\u0007\u0003\u0000\u0000V\u001d\u0001\u0000\u0000\u0000"+
		"WX\u0007\u0004\u0000\u0000XY\u0001\u0000\u0000\u0000YZ\u0006\u000e\u0001"+
		"\u0000Z\u001f\u0001\u0000\u0000\u0000[]\u0003\u001c\r\u0000\\[\u0001\u0000"+
		"\u0000\u0000]^\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000^_\u0001"+
		"\u0000\u0000\u0000_!\u0001\u0000\u0000\u0000`a\u0005*\u0000\u0000ab\u0001"+
		"\u0000\u0000\u0000bc\u0006\u0010\u0002\u0000cd\u0006\u0010\u0003\u0000"+
		"d#\u0001\u0000\u0000\u0000\u0007\u0000\u00010EKR^\u0004\u0005\u0001\u0000"+
		"\u0000\u0001\u0000\u0004\u0000\u0000\u0007\u0003\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}